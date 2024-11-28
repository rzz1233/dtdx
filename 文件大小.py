# 获取一个目录中所有文件的大小总和
import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        print(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename) #将文件路径组合成完整的路径。
            # 跳过不存在或无法访问的文件
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)  #os.path.getsize(file_path)：返回文件大小（以字节为单位）。
    return total_size

# 示例用法：获取当前目录下所有文件的大小总和
directory_path = "."  # 可以换成你要统计的目录路径
size_in_bytes = get_directory_size(directory_path)
print(f"文件大小总和: {size_in_bytes} bytes")
