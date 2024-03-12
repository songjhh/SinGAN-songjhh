import netCDF4 as nc
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 打开 NetCDF 文件
nc_file = nc.Dataset(
    # "/Users/jianghouhong/code/songjhh/depth-learning/SinGAN-songjhh/original-data/2020_month_x4/202001.nc4",
    "/Users/jianghouhong/code/songjhh/depth-learning/SinGAN-songjhh/test/3B-MO.MS.MRG.3IMERG.20200101-S000000-E235959.01.V07B.HDF5.nc4",
    "r",
)
precip_var = nc_file.variables["precipitation"]
print(precip_var.name, precip_var.units)
# nc_file = nc.Dataset("./data_resampled_x1.nc", "r")

# # 获取特定变量的维度
# test_var = nc_file.variables['precipitationCal']
# dimensions = test_var.dimensions

# # 获取每个维度的步长或间隔（像元大小）
# pixel_sizes = []
# for dim_name in dimensions:
#     dim_size = len(nc_file.dimensions[dim_name])
#     dim_var = nc_file.variables[dim_name]
#     dim_step = (dim_var[-1] - dim_var[0]) / (dim_size - 1)
#     pixel_sizes.append(dim_step)

# # 打印每个维度的像元大小
# print("Pixel sizes for variable 'test':", pixel_sizes)

# 查看文件中的变量名称
# print("Variables in the file:", nc_file.variables.keys())

# 获取经度、纬度和降水数据的变量
# lon_var = nc_file.variables["lon"]
# lat_var = nc_file.variables["lat"]
# precip_var = np.squeeze(precip_var)

# np.savetxt(
#     "./tttt.txt",
#     precip_var,
# )
# sns.set()
# plt.close("all")
# plt.figure(figsize=(32, 12))
# ax = sns.heatmap(precip_var, vmin=0, yticklabels=False, xticklabels=False, vmax=np.max(precip_var))
# plt.title("model")
# plt.savefig("./ttt.png")
# time_var = nc_file.variables["time"]

# print(precip_var[0])

# 获取经度和纬度范围
# lon_min = lon_var[:].min()
# lon_max = lon_var[:].max()
# lat_min = lat_var[:].min()
# lat_max = lat_var[:].max()
# print("Longitude range:", lon_min, lon_max)
# print("Latitude range:", lat_min, lat_max)


# 输入文件路径
# input_nc4_file = "./20190309.nc4"
# # 输出文件路径
# output_nc4_file = "./output.nc4"
# # 要裁剪的经纬度范围（xmin, ymin, xmax, ymax）
# extent = (lon_min, lat_min, lon_max, lat_max)
# # 重采样因子
# resample_factor = 4

# # 打开输入nc4文件
# input_ds = gdal.Open(input_nc4_file)

# # 设置裁剪的范围
# xmin, ymin, xmax, ymax = extent
# input_ds.SetGeoTransform((xmin, (xmax - xmin) / input_ds.RasterXSize, 0, ymax, 0, - (ymax - ymin) / input_ds.RasterYSize))

# # 执行裁剪
# clipped_ds = gdal.Translate("", input_ds, projWin=[xmin, ymax, xmax, ymin])

# # 设置重采样
# output_ds = gdal.Translate(output_nc4_file, clipped_ds, format='NetCDF', xRes=input_ds.RasterXSize * resample_factor, yRes=input_ds.RasterYSize * resample_factor)

# # 关闭数据集
# input_ds = None
# clipped_ds = None
# output_ds = None

# print("裁剪和重采样完成")


# # 关闭文件
nc_file.close()
