import os
import shutil
from unittest.mock import patch

import cabarchive
import pytest

from python_extrac.cab import unpack_cab


@pytest.fixture
def create_cab_file(tmp_path):
    # 创建一个临时 CAB 文件用于测试
    cab_file_path = tmp_path / "test.cab"
    test_file_content = b"Hello, CAB World!"

    arc = cabarchive.CabArchive()
    arc["test.txt"] = cabarchive.CabFile(test_file_content)
    with open(cab_file_path, "wb") as f:
        f.write(arc.save())

    yield cab_file_path

    os.remove(cab_file_path)


def test_unpack_cab(create_cab_file, tmp_path, capfd):
    output_folder = tmp_path / "output"

    # 调用 unpack_cab 方法解压 CAB 文件
    unpack_cab(create_cab_file, output_folder)

    # 验证解压结果
    extracted_file_path = output_folder / "test.txt"
    assert extracted_file_path.exists(), "解压的文件不存在"

    with open(extracted_file_path, "rb") as f:
        content = f.read()

    assert content == b"Hello, CAB World!", "文件内容不匹配"

    # 捕获并断言print内容
    captured = capfd.readouterr()
    assert "NotSupportedError" not in captured.out
    assert "CorruptionError" not in captured.out
    clean_output_folder(output_folder)


def test_unpack_cab_with_corrupted_file(tmp_path, capfd):
    corrupted_cab_file_path = tmp_path / "corrupted.cab"

    # 创建一个假的、损坏的 CAB 文件
    with open(corrupted_cab_file_path, "wb") as f:
        f.write(b"This is not a valid CAB file")

    output_folder = tmp_path / "output"

    # 调用 unpack_cab 方法解压损坏的 CAB 文件
    unpack_cab(corrupted_cab_file_path, output_folder)

    # 验证输出目录为空，因为解压失败
    assert not any(output_folder.iterdir()), "输出目录应该为空"

    # 捕获并断言print内容
    captured = capfd.readouterr()
    assert "CorruptionError" in captured.out
    shutil.rmtree(output_folder)


@patch(
    "cabarchive.CabArchive", side_effect=cabarchive.NotSupportedError("Not supported")
)
def test_unpack_cab_with_not_supported_file(mock_cabarchive, tmp_path, capfd):
    not_supported_cab_file_path = tmp_path / "not_supported.cab"

    # 创建一个假的 CAB 文件
    with open(not_supported_cab_file_path, "wb") as f:
        f.write(b"MSCF\x00\x00\x00\x00")

    output_folder = tmp_path / "output"

    # 调用 unpack_cab 方法解压不支持的 CAB 文件
    unpack_cab(not_supported_cab_file_path, output_folder)

    # 验证输出目录为空，因为解压失败
    assert not any(output_folder.iterdir()), "输出目录应该为空"

    # 捕获并断言print内容
    captured = capfd.readouterr()
    assert "NotSupportedError" in captured.out
    shutil.rmtree(output_folder)
