import torch
import functions
import size
import generate
import argparse
import config
import torch.nn as nn
from pathlib import Path
from netCDF4 import Dataset as ncdataset
import numpy as np


if __name__ == "__main__":
    # 处理配置
    parser = config.get_arguments()
    parser.add_argument("--model_dir", default="")
    parser.add_argument(
        "--sr_factor", help="super resolution factor", type=float, default=4
    )
    parser.add_argument("--mode", help="task to be done", default="SR")
    parser.set_defaults(nc_im=1)
    parser.set_defaults(nc_z=1)
    parser.set_defaults(alpha=30)

    opt = parser.parse_args()
    Gs = torch.load(opt.model_dir + "/Gs.pth")
    Zs = torch.load(opt.model_dir + "/Zs.pth")
    reals = torch.load(opt.model_dir + "/reals.pth")
    NoiseAmp = torch.load(opt.model_dir + "/NoiseAmp.pth")

    path = Path("/content/testing-set")
    for testing_file in path.rglob("*.nc4"):
        saveop = str(testing_file)[-12:-4]
        opt = parser.parse_args()
        opt = config.post_config(opt)
        Zs_sr = []
        reals_sr = []
        NoiseAmp_sr = []
        Gs_sr = []

        real = reals[-1]  # read_image(opt)
        real_ = real
        in_scale, iter_num = functions.calc_init_scale(opt)
        opt.scale_factor = 1 / in_scale
        opt.scale_factor_init = 1 / in_scale
        opt.mode = "train"

        dst = ncdataset(testing_file)
        target = dst.variables["precipitationCal"]
        target = np.squeeze(target)
        maxsd = [np.max(target)]

        for j in range(1, iter_num + 1, 1):
            real_ = size.mimresize(real_, pow(1 / opt.scale_factor, 1), maxsd, opt)
            reals_sr.append(real_)
            Gs_sr.append(Gs[-1])
            NoiseAmp_sr.append(NoiseAmp[-1])
            z_opt = torch.full(real_.shape, 0, device=opt.device)
            m = nn.ZeroPad2d(5)
            z_opt = m(z_opt)
            Zs_sr.append(z_opt)

        opt.num_samples = 1
        out = generate.SinGAN_generate(
            Gs_sr, Zs_sr, reals_sr, NoiseAmp_sr, opt, maxsd, in_s=reals_sr[0]
        )
        out = out[
            :,
            :,
            0 : int(opt.sr_factor * reals[-1].shape[2]) - 1,
            0 : int(opt.sr_factor * reals[-1].shape[3]),
        ]
        outt = size.denorm(out)
        inp = outt[-1, -1, :, :].to(torch.device("cpu"))
        inp = inp.numpy()
        inpp = inp * maxsd
        np.savetxt(
            "/content/drive/MyDrive/code/SinGAN-songjhh/Results/%s.txt" % saveop, inpp
        )
        np.savetxt(
            "/content/drive/MyDrive/code/SinGAN-songjhh/Original/%s.txt" % saveop,
            target,
        )
