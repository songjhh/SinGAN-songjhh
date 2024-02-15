import netCDF4 as nc

# 打开 NetCDF 文件
nc_file = nc.Dataset('SinGAN-songjhh/data/training-set/20190309.nc4', 'r')

# 获取特定变量的维度
test_var = nc_file.variables['precipitationCal']
dimensions = test_var.dimensions

# 获取每个维度的步长或间隔（像元大小）
pixel_sizes = []
for dim_name in dimensions:
    dim_size = len(nc_file.dimensions[dim_name])
    dim_var = nc_file.variables[dim_name]
    dim_step = (dim_var[-1] - dim_var[0]) / (dim_size - 1)
    pixel_sizes.append(dim_step)

# 打印每个维度的像元大小
print("Pixel sizes for variable 'test':", pixel_sizes)

# 查看文件中的变量名称
# print("Variables in the file:", nc_file.variables.keys())

# 获取经度、纬度和降水数据的变量
# lon_var = nc_file.variables['lon']
# lat_var = nc_file.variables['lat']
# precip_var = nc_file.variables['precipitationCal']
# time_var = nc_file.variables['time']

# print(precip_var)

# 获取经度和纬度范围
# lon_min = lon_var[:].min()
# lon_max = lon_var[:].max()
# lat_min = lat_var[:].min()
# lat_max = lat_var[:].max()
# print("Longitude range:", lon_min, lon_max)
# print("Latitude range:", lat_min, lat_max)

# # 获取经度和纬度的分辨率
# lon_resolution = lon_var[1] - lon_var[0]
# lat_resolution = lat_var[1] - lat_var[0]
# print("Longitude resolution:", lon_resolution)
# print("Latitude resolution:", lat_resolution)

# 关闭文件
nc_file.close()
