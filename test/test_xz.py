import lzma
import os
from tempfile import TemporaryDirectory

import pytest


def unpack_xz(file_path: str, output_path: str, chunk_size: int = 1024 * 1024) -> None:
    with lzma.open(file_path, "rb") as f_in, open(output_path, "wb") as f_out:
        while True:
            chunk = f_in.read(chunk_size)
            if not chunk:
                break
            f_out.write(chunk)


@pytest.fixture
def sample_data():
    data = b"Hello, world!"
    with TemporaryDirectory() as temp_dir:
        input_file = os.path.join(temp_dir, "sample.xz")
        output_file = os.path.join(temp_dir, "sample.txt")

        with lzma.open(input_file, "wb") as f:
            f.write(data)

        yield input_file, output_file, data


def test_unpack_xz(sample_data):
    input_file, output_file, expected_data = sample_data
    unpack_xz(input_file, output_file)

    with open(output_file, "rb") as f:
        actual_data = f.read()

    assert actual_data == expected_data
