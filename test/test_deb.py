import io
import os
import shutil
import tarfile
from pathlib import Path
from subprocess import run

import arpy
import pytest

from python_extrac.deb import unpack_deb


@pytest.fixture
def create_deb_file(tmp_path):
    deb_file_path = Path("mypackage.deb")
    if not deb_file_path.exists():
        os.system(
            'docker run --rm -v "$(pwd):/workdir" debian:stable-slim bash /workdir/make_deb_package.sh'
        )
    yield deb_file_path
    deb_file_path.unlink()  # 测试后删除 DEB 文件


def test_unpack_deb(create_deb_file):
    print(">>>>>>>>>>>>>>>>", create_deb_file)
    output_dir = Path.cwd() / "unpacked"
    unpack_deb(create_deb_file, output_dir)
    assert (output_dir / "data/usr/local/bin/helloworld").exists()
    with open(str(output_dir / "data/usr/local/bin/helloworld")) as f:
        content = f.read().strip()
    assert content == "echo Hello, World!"

    shutil.rmtree(output_dir)
