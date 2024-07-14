import shutil

import py7zr
import pytest

from python_extrac.py7z import unpack_7z


@pytest.fixture
def create_sample_7z_file(tmp_path):
    sample_dir = tmp_path / "sample"
    sample_dir.mkdir()

    # 创建示例文件
    sample_file = sample_dir / "sample.txt"
    with open(sample_file, "w") as f:
        f.write("This is a test file.")

    # 创建 7z 文件
    sample_7z_path = tmp_path / "sample.7z"
    with py7zr.SevenZipFile(sample_7z_path, mode="w") as archive:
        archive.write(sample_file, "sample.txt")

    yield sample_7z_path

    # 测试后删除 7z 文件
    sample_7z_path.unlink()


def test_unpack_7z(create_sample_7z_file, tmp_path):
    output_dir = tmp_path / "unpacked"
    unpack_7z(create_sample_7z_file, output_dir)

    # 验证解压缩后的文件
    extracted_file = output_dir / "sample.txt"
    assert extracted_file.exists()

    with open(extracted_file) as f:
        content = f.read().strip()

    assert content == "This is a test file."

    shutil.rmtree(output_dir)
