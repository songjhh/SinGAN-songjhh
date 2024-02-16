import xarray as xr
import dask.array as da

# 打开NetCDF文件
ds = xr.open_dataset("SinGAN-songjhh/data/training-set/20190309.nc4")

# 重采样／升采样或再网格化
ds_resampled_x1 = ds["precipitationCal"].interp(
    lat=da.arange(35, 39.9, 0.1), lon=da.arange(-100, -89.9, 0.1)
)
ds_resampled_x1.to_netcdf("SinGAN-songjhh/test/data_resampled_x1.nc4")
ds_resampled_x4 = ds["precipitationCal"].interp(
    lat=da.arange(35, 40, 0.4), lon=da.arange(-100, -89.9, 0.4)
)
ds_resampled_x4.to_netcdf("SinGAN-songjhh/test/data_resampled_x4.nc4")


ds_x1 = xr.open_dataset("SinGAN-songjhh/test/data_resampled_x1.nc4")
print(ds_x1["precipitationCal"])

ds_x2 = xr.open_dataset("SinGAN-songjhh/test/data_resampled_x4.nc4")
print(ds_x2["precipitationCal"])
