import os
from pathlib import Path

import cabarchive
from cabarchive import CabFile


def extract_cab_file(input_path, output_folder):
    """
    解压 CAB 文件，并提取其中的所有文件。

    :param input_path: 输入的 CAB 文件路径
    :param output_folder: 输出的解压后文件的文件夹路径
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开 CAB 文件
    with open(input_path, "rb") as f:
        archive = cabarchive.CabArchive(f.read())
        print(archive)
        # 提取所有文件
        for filename in archive:
            cff: CabFile = archive[filename]
            print(cff)
            filename = filename.replace("\\", "/")
            print(filename)
            output_path: str = os.path.join(output_folder, filename)
            print(output_path)
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as out_file:
                out_file.write(cff.buf)


# 示例使用
try:
    extract_cab_file("mszip.cab", "output")
    print("解压成功")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("解压失败", e)
