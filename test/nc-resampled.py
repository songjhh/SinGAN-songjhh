import xarray as xr
import dask.array as da
import os


root_dir = "SinGAN-songjhh/original-data/2020_1"
x1_dir = "SinGAN-songjhh/original-data/2020_1_x1/"
x4_dir = "SinGAN-songjhh/original-data/2020_1_x4/"
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ds = xr.open_dataset(os.path.join(root, file))
        # ds_subset = ds["precipitation"].sel(lat=slice(20, 30), lon=slice(106, 110))
        ds_subset = ds["precipitation"]
        # 获取文件名的起始位置和结束位置
        start_index = file.find("3B-DAY.MS.MRG.3IMERG.")
        end_index = file.find("-S")
        # 提取日期部分并添加.nc4后缀
        new_file_name = file[21:end_index] + ".nc4"

        ds_resampled_x1 = ds_subset.interp(
            lat=da.arange(20, 40, 0.1), lon=da.arange(100, 120, 0.1)
        )
        ds_resampled_x1.to_netcdf(x1_dir + new_file_name)

        ds_resampled_x4 = ds_subset.interp(
            lat=da.arange(20, 40, 0.4), lon=da.arange(100, 120, 0.4)
        )
        ds_resampled_x4.to_netcdf(x4_dir + new_file_name)


ds_x1 = xr.open_dataset(x1_dir + "20200101.nc4")
print(ds_x1["precipitation"])
print(len(ds_x1["precipitation"].lat))
print(len(ds_x1["precipitation"].lon))
ds_x4 = xr.open_dataset(x4_dir + "20200101.nc4")
print(ds_x4["precipitation"])
print(len(ds_x4["precipitation"].lat))
print(len(ds_x4["precipitation"].lon))

# ds_test = xr.open_dataset("SinGAN-songjhh/test/20190309.nc4")
# print(ds_test["precipitationCal"].lat)
# print(len(ds_test["precipitationCal"].lat))
# print(len(ds_test["precipitationCal"].lon))
# ds_test2 = xr.open_dataset("SinGAN-songjhh/data/202001_nc4_0.4/3B-DAY.MS.MRG.3IMERG.20200101-S000000-E235959.V07B.nc4")
# print(ds_test2["Band1"])
