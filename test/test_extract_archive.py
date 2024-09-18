import sys
from unittest.mock import patch

from python_extrac.utils import extract_archive

_PYTHON = sys.executable


@patch("python_extrac.utils.get_file_format")
@patch("python_extrac.utils.call")
def test_extract_archive_with_output(mock_call, mock_get_file_format):
    mock_get_file_format.return_value = "zip"
    extract_archive("test_file.zip", "output_dir")
    defenc = sys.getfilesystemencoding()
    mock_call.assert_called_with(
        [_PYTHON, "-m", "zipfile", "--metadata-encoding", defenc, "-e", "test_file.zip", "output_dir"]
    )


@patch("python_extrac.utils.get_file_format")
@patch("python_extrac.utils.call")
def test_extract_archive_without_output(mock_call, mock_get_file_format):
    mock_get_file_format.return_value = "zip"
    extract_archive("test_file.zip")
    defenc = sys.getfilesystemencoding()
    mock_call.assert_called_with(
        [_PYTHON, "-m", "zipfile", "--metadata-encoding", defenc, "-e", "test_file.zip", "output_dir", "test_file.zip"]
    )


@patch("python_extrac.utils.get_file_format")
@patch("python_extrac.utils.call")
def test_extract_archive_with_a_format(mock_call, mock_get_file_format):
    mock_get_file_format.return_value = "a"
    extract_archive("test_file.a")
    mock_call.assert_called_with([_PYTHON, "-m", "python_extrac.ar", "test_file.a"])
