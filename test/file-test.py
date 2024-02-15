import os
import fnmatch


def find_file(root_dir, file_pattern):
    # 遍历根目录下的所有子目录和文件
    for root, dirs, _ in os.walk(root_dir):
        # 在当前目录下查找匹配的文件名模式
        for dir in dirs:
            for _, _, files in os.walk(os.path.join(root_dir, dir)):
                for file in files:
                    if fnmatch.fnmatch(file, file_pattern):
                        # 如果找到匹配的文件，则返回完整路径
                        return os.path.join(root, dir, file)
    # 如果未找到匹配的文件，则返回空字符串


# 指定根目录和文件名模式
root_dir = "/Users/jianghouhong/code/other/depth-learning/SinGAN-songjhh/TrainedModels/20190309"
file_pattern = "Gs.pth"

# 查找文件
file_path = find_file(root_dir, file_pattern)

# 打印文件路径
if file_path:
    print("文件路径：", file_path)
else:
    print("未找到匹配的文件。")
