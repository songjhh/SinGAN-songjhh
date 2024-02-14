def generate_dir2save(opt):
    dir2save = None
    if (opt.mode == "train") | (opt.mode == "SR_train"):
        dir2save = "TrainedModels/%s/scale_factor=%f,alpha=%d" % (
            opt.input_name,
            opt.scale_factor_init,
            opt.alpha,
        )
    elif opt.mode == "SR":
        dir2save = "%s/SR/%s" % (opt.out, opt.sr_factor)

    return dir2save
