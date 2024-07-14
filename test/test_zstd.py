from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
import zstandard as zstd

from python_extrac.zstd import unpack_zstd


@pytest.fixture
def sample_data():
    data = b"Hello, world!"
    with TemporaryDirectory() as temp_dir:
        input_file = Path(temp_dir) / "sample.zst"
        output_file = Path(temp_dir) / "sample.txt"

        # Compress the data
        cctx = zstd.ZstdCompressor()
        with open(input_file, "wb") as f:
            f.write(cctx.compress(data))

        yield input_file, output_file, data


def test_unpack_zstd(sample_data):
    input_file, output_file, expected_data = sample_data
    unpack_zstd(input_file, output_file)

    with open(output_file, "rb") as f:
        actual_data = f.read()

    assert actual_data == expected_data


if __name__ == "__main__":
    pytest.main()
