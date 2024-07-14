import bz2

from python_extrac.utils import open_and_extract


def unpack_bz2(file_path: str, output_path: str = None, *args) -> None:
    """
    Extract bz2 archive
    """

    open_and_extract(
        file_path, extension=".bz2", _open=bz2.open, output_path=output_path
    )
