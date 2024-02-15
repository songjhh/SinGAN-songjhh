import netCDF4 as nc
import matplotlib.pyplot as plt

# 打开 NetCDF 文件
nc_file = nc.Dataset('SinGAN-songjhh/data/training-set/20190309.nc4')

# 获取图像数据
image_data = nc_file.variables['precipitationCal'][:]

# 关闭文件
nc_file.close()

# 显示图像
plt.imshow(image_data, cmap='viridis')  # 选择色彩映射，例如 'viridis', 'gray', 'jet' 等
plt.colorbar()  # 显示颜色条
plt.show()