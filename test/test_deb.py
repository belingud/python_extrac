import shutil
from pathlib import Path
from subprocess import check_call

import pytest

from python_extrac.deb import unpack_deb


@pytest.fixture
def create_deb_file(tmp_path):
    deb_file_path = Path("mypackage.deb").resolve()
    if not deb_file_path.exists():
        check_call(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                '"$(pwd):/workdir"',
                "debian:stable-slim",
                "bash",
                "/workdir/make_deb_package.sh",
            ]
        )
    yield deb_file_path


def test_unpack_deb(create_deb_file):
    output_dir = Path.cwd() / "unpacked"
    unpack_deb(create_deb_file, output_dir)
    assert (output_dir / "data/usr/local/bin/helloworld").exists()
    with open(str(output_dir / "data/usr/local/bin/helloworld")) as f:
        content = f.read().strip()
    assert content == "echo Hello, World!"

    shutil.rmtree(output_dir)
