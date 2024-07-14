import shutil
from subprocess import call

import pytest

from python_extrac.ar import unpack_ar


@pytest.fixture
def setup_ar_file(tmp_path):
    # 创建一个临时 ar 文件用于测试
    ar_file_path = tmp_path / "test.ar"
    file_content = b"Hello, World!"

    with open(tmp_path / "file.txt", "wb") as f:
        f.write(file_content)

    call(f"ar r {ar_file_path} {tmp_path / 'file.txt'}", shell=True)

    yield ar_file_path

    shutil.rmtree(tmp_path)


def test_unpack_ar(setup_ar_file, tmp_path):
    output_path = tmp_path / "output"

    # 调用 unpack_ar 方法
    unpack_ar(setup_ar_file, output_path)

    # 验证解压结果
    extracted_file_path = output_path / "file.txt"
    assert extracted_file_path.exists(), "解压的文件不存在"

    with open(extracted_file_path, "rb") as f:
        content = f.read()

    assert content == b"Hello, World!", "文件内容不匹配"

    shutil.rmtree(output_path)
