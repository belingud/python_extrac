import gzip
import os
import shutil

import pytest

from python_extrac.utils import open_and_extract


@pytest.fixture
def setup_gz_file(tmp_path):
    # 创建一个临时 gz 文件用于测试
    gz_file_path = tmp_path / "test.txt.gz"
    file_content = b"Hello, World!"

    with open(tmp_path / "test.txt", "wb") as f:
        f.write(file_content)

    # 使用 gz 命令创建 gz 文件 (假设系统上有 gz 命令)
    os.system(f"gzip {tmp_path / 'test.txt'}")

    yield gz_file_path

    shutil.rmtree(tmp_path)


def test_open_and_extract(setup_gz_file, tmp_path):
    output_path = tmp_path / "output"

    # 调用 open_and_extract 方法
    open_and_extract(setup_gz_file, output_path, extension=".gz", _open=gzip.open)

    # 验证解压结果
    extracted_file_path = output_path / "test.txt"
    assert extracted_file_path.exists(), "解压的文件不存在"

    with open(extracted_file_path, "rb") as f:
        content = f.read()

    assert content == b"Hello, World!", "文件内容不匹配"

    shutil.rmtree(output_path)


def test_open_and_extract_without_output_path(setup_gz_file, tmp_path):
    # 调用 open_and_extract 方法, 不传递 output_path
    open_and_extract(setup_gz_file, extension=".gz", _open=gzip.open)

    # 验证解压结果
    extracted_file_path = setup_gz_file.with_suffix("")
    assert extracted_file_path.exists(), "解压的文件不存在"

    with open(f"{extracted_file_path}/test.txt", "rb") as f:
        content = f.read()

    assert content == b"Hello, World!", "文件内容不匹配"

    shutil.rmtree(extracted_file_path)
