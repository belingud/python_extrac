import bz2
import gzip
import lzma
import os
import shutil
import tarfile
import zipfile

import arpy
import py7zr
import zstandard as zstd


# 创建示例文件
def create_sample_file(filename, content="This is a test file"):
    with open(filename, "w") as f:
        f.write(content)


sample_file = "sample.txt"
create_sample_file(sample_file)

# 创建 tar 文件
with tarfile.open("sample.tar", "w") as tar:
    tar.add(sample_file)

# 创建 tar.gz 文件
with tarfile.open("sample.tar.gz", "w:gz") as tar:
    tar.add(sample_file)

# 创建 tar.bz2 文件
with tarfile.open("sample.tar.bz2", "w:bz2") as tar:
    tar.add(sample_file)

# 创建 tar.xz 文件
with tarfile.open("sample.tar.xz", "w:xz") as tar:
    tar.add(sample_file)

# 创建 zip 文件
with zipfile.ZipFile("sample.zip", "w") as zipf:
    zipf.write(sample_file)

# 创建 gz 文件
with open(sample_file, "rb") as f_in:
    with gzip.open("sample.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

# 创建 bz2 文件
with open(sample_file, "rb") as f_in:
    with bz2.open("sample.bz2", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

# 创建 xz 文件
with open(sample_file, "rb") as f_in:
    with lzma.open("sample.xz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

# 创建 7z 文件
with py7zr.SevenZipFile("sample.7z", "w") as archive:
    archive.write(sample_file)

# 创建zstd文件
with open(sample_file, "rb") as f_in:
    with open("sample.zstd", "wb") as f_out:
        compressor = zstd.ZstdCompressor()
        stream_compressor = compressor.stream_writer(f_out)
        stream_compressor.write(f_in.read())
        stream_compressor.close()

# 创建ar文件
os.system(f"ar qc sample.ar {sample_file}")

# 创建 rar 文件
os.system(f"rar a sample.rar {sample_file}")

# 创建 Z 文件
os.system(f"compress -c {sample_file} > sample.Z")
os.system("compress -c sample.tar > sample.tar.Z")

# 创建 arj 文件，在linux中创建

# 创建 cab 文件，在windows中创建

# 清理示例文件
# os.remove(sample_file)
