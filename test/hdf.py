import h5py
from netCDF4 import Dataset

# 打开HDF5文件
hdf5_file = h5py.File(
    "../original-data/2020_month_hdf/3B-MO.MS.MRG.3IMERG.20200101-S000000-E235959.01.V07B.HDF5",
    "r",
)

# 创建NetCDF4文件
nc4_file = Dataset("output_file.nc", "w", format="NETCDF4")

# with h5py.File(
#     "../original-data/2020-every-month/3B-MO.MS.MRG.3IMERG.20200101-S000000-E235959.01.V07B.HDF5",
#     "r",
# ) as file:
#     all_vars = list(file.keys())
#     print(all_vars)
#     for name in file["Grid"]:
#         print(name)
#     print(file["Grid"]["lon"])
    # 打印文件中的数据集和组名称
    # print("Datasets:")
    # for name in file.keys():
    #     print(name)

    # print("\nGroups:")
    # for group in file.values():
    #     print(group.name)
    #     print(group)

# 遍历HDF5文件中的数据集
for dataset_name in hdf5_file.keys():
    print(dataset_name)
    # 获取数据集
    dataset = hdf5_file[dataset_name]
    print(dataset)

    for name in dataset:
      print(name)
      print(dataset[name])
      
        # nc_variable = nc4_file.createVariable(
        #     name, dataset[name].dtype, dataset[name].shape
        # )

    # 创建相应的NetCDF4变量
    # nc_variable = nc4_file.createVariable(dataset_name, dataset.dtype, dataset.shape)

    # 将数据从HDF5复制到NetCDF4
    # nc_variable[:] = dataset[:]

# 关闭文件
hdf5_file.close()
nc4_file.close()
