from unittest.mock import patch

from python_extrac.utils import get_file_format


@patch("filetype.guess")
def test_get_file_format_known_format(mock_guess):
    mock_guess.return_value.extension = "zip"
    result = get_file_format("test_file.zip")
    assert result == "zip"


@patch("filetype.guess")
def test_get_file_format_unknown_format(mock_guess):
    mock_guess.return_value = None
    result = get_file_format("test_file.unknown")
    assert result is None


@patch("filetype.guess")
def test_get_file_format_a_format(mock_guess):
    mock_guess.return_value.extension = "ar"
    result = get_file_format("test_file.a")
    assert result == "a"


@patch("filetype.guess")
def test_get_file_format_rar_format(mock_guess):
    mock_guess.return_value.extension = "rar"
    result = get_file_format("test_file.rar")
    assert result == "rar"


@patch("filetype.guess")
def test_get_file_format_cbr_format(mock_guess):
    mock_guess.return_value.extension = "rar"
    result = get_file_format("test_file.cbr")
    assert result == "rar"


@patch("filetype.guess")
def test_get_file_format_7z_format(mock_guess):
    mock_guess.return_value.extension = "7z"
    result = get_file_format("test_file.7z")
    assert result == "7z"


@patch("filetype.guess")
def test_get_file_format_tar_gz_format(mock_guess):
    mock_guess.return_value.extension = "gz"
    result = get_file_format("test_file.tar.gz")
    assert result == "tar.gz"


@patch("filetype.guess")
def test_get_file_format_tar_bz_format(mock_guess):
    mock_guess.return_value.extension = "bz2"
    result = get_file_format("test_file.tar.bz")
    assert result == "tar.bz"


@patch("filetype.guess")
def test_get_file_format_tar_bz2_format(mock_guess):
    mock_guess.return_value.extension = "bz2"
    result = get_file_format("test_file.tar.bz2")
    assert result == "tar.bz2"


@patch("filetype.guess")
def test_get_file_format_zstd_format(mock_guess):
    mock_guess.return_value.extension = "zst"
    result = get_file_format("test_file.zstd")
    assert result == "zstd"


@patch("filetype.guess")
def test_get_file_format_zst_format(mock_guess):
    mock_guess.return_value.extension = "zst"
    result = get_file_format("test_file.zst")
    assert result == "zst"


@patch("filetype.guess")
def test_get_file_format_Z_format(mock_guess):  # noqa
    mock_guess.return_value.extension = "Z"
    result = get_file_format("test_file.Z")
    assert result == "Z"


@patch("filetype.guess")
def test_get_file_format_tar_format(mock_guess):
    mock_guess.return_value.extension = "tar"
    result = get_file_format("test_file.tar")
    assert result == "tar"


@patch("filetype.guess")
def test_get_file_format_jar_format(mock_guess):
    mock_guess.return_value.extension = "zip"
    result = get_file_format("test_file.jar")
    assert result == "zip"
