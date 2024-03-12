import xarray as xr
import dask.array as da
import os
from netCDF4 import Dataset as ncdataset


root_dir = "../original-data/2020_month_hdf/"
x1_dir = "../original-data/2020_month_x1/"
x4_dir = "../original-data/2020_month_x4/"
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ds2 = xr.open_dataset(os.path.join(root, file), group="Grid")
        ds_subset = ds2["precipitation"]

        # 对变量进行插值
        new_file_name = "2020" + str(file)[-12:-10] + ".nc4"
        # ds_resampled_x1 = ds_subset.interp(
        #     lat=da.arange(24, 36, 0.1), lon=da.arange(90, 122, 0.1)
        # )
        # ds_resampled_x1.to_netcdf(x1_dir + new_file_name)
        # print(len(ds_resampled_x1.lat))
        # print(len(ds_resampled_x1.lon))

        ds_resampled_x4 = ds_subset.interp(
            lat=da.arange(24, 36, 0.4), lon=da.arange(90, 122, 0.4)
        )
        ds_resampled_x4.to_netcdf(x4_dir + new_file_name)


        # # 创建包含插值所需经纬度范围的新数据集
        # new_lat = da.arange(20, 32, 0.1)
        # new_lon = da.arange(106, 118, 0.1)
        # ds_interp_coords = xr.Dataset(coords={"lat": new_lat, "lon": new_lon})
        # ds_subset = ds_subset.sel(lat=slice(ds_subset['lat'].min(), ds_subset['lat'].max()),
        #                    lon=slice(ds_subset['lon'].min(), ds_subset['lon'].max()))
        # ds_resampled_x1 = ds_subset.interp(coords=ds_interp_coords, method="linear")