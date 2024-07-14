from unittest.mock import patch

from python_extrac.utils import extract_to


@patch("python_extrac.utils.get_file_format")
def test_extract_to_with_extension(mock_get_file_format):
    mock_get_file_format.return_value = "zip"
    result = extract_to("test_file.zip", "work_dir", "zip")
    assert result == "work_dir/test_file"


@patch("python_extrac.utils.get_file_format")
def test_extract_to_without_extension(mock_get_file_format):
    mock_get_file_format.return_value = "zip"
    result = extract_to("test_file.zip", "work_dir")
    assert result == "work_dir/test_file"
