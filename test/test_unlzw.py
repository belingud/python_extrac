import io
from pathlib import Path

import pytest

from python_extrac.unlzw import unlzw_chunked


def generate_compressed_data():
    # This is a simplified example; in practice, you would use a real compressed file
    return b"\x1f\x9d\x90" + b"\x00" * 1024


def test_unlzw_chunked_normal():
    # compressed_data = generate_compressed_data()
    filepath = Path(__file__).resolve().parent / "archives/sample.Z"
    file = filepath.open("rb")
    decompressed_data = b""
    # for chunk in unlzw_chunked(file):
    #     print('chunk::::::::', chunk)
    #     decompressed_data += chunk
    decompressed_data = b"".join(unlzw_chunked(file))
    print(decompressed_data)
    # assert decompressed_data == b'\x00' * 1024  # Assuming the decompressed data is all zeros


def test_unlzw_chunked_invalid_header():
    invalid_header_data = b"\x1f\x9e\x01"  # Invalid header
    file = io.BytesIO(invalid_header_data)
    with pytest.raises(
        ValueError, match="Invalid Header Flags Byte: Incorrect magic bytes"
    ):
        next(unlzw_chunked(file))


def test_unlzw_chunked_short_input():
    short_input_data = b"\x1f\x9d"  # Input too short
    file = io.BytesIO(short_input_data)
    with pytest.raises(
        ValueError, match="Invalid Input: Length of input too short for processing"
    ):
        next(unlzw_chunked(file))


def test_unlzw_chunked_invalid_flags():
    invalid_flags_data = b"\x1f\x9d\x61"  # Invalid flags
    file = io.BytesIO(invalid_flags_data)
    with pytest.raises(
        ValueError, match="Invalid Header Flags Byte: Flag byte contains invalid data"
    ):
        next(unlzw_chunked(file))


def test_unlzw_chunked_invalid_max_code_size():
    invalid_max_code_size_data = b"\x1f\x9d\x08"  # Invalid max code size
    file = io.BytesIO(invalid_max_code_size_data)
    with pytest.raises(
        ValueError, match="Invalid Header Flags Byte: Max code size bits out of range"
    ):
        next(unlzw_chunked(file))


def test_unlzw_chunked_invalid_code():
    # This test case assumes that the function will raise an error if an invalid code is encountered
    invalid_code_data = generate_compressed_data() + b"\xff"  # Adding an invalid code
    file = io.BytesIO(invalid_code_data)
    with pytest.raises(ValueError, match="Invalid Data: Invalid code detected"):
        for chunk in unlzw_chunked(file):
            pass


if __name__ == "__main__":
    test_unlzw_chunked_normal()
