#!/usr/bin/env python
# coding: utf-8
"""
$ pip install --upgrade setuptools wheel twine
$ python3 setup.py sdist bdist_wheel
$ twine upload -u belingud -p [file_path]

$ pyinstaller -F python_extrac/extrac.py

add docs
$ sudo apt-get install python3-sphinx

git push
$ git add .
$ git commit -m 'update'
$ git push
$ git checkout master
$ git merge dev
$ git push
"""
import sys
import subprocess
from loguru import logger
import click

usage = """
$ python release.py pypi patch
    0.0.1 --> 0.0.2
$ python release.py pypi minor:
    0.0.1 --> 0.1.0
$ python release.py pypi major:
    0.0.1 --> 1.0.0
"""
# VALUE_TO_BUMP = {"patch": 2, "minor": 1, "major": 0}

# build a docker image or release a pypi package
# in first arg passed in command line
# shoud be : docker or pypi
RELEASE_PYPI = "pypi" == sys.argv[1]

if RELEASE_PYPI:
    # patch minor major
    VERSION_BUMP = sys.argv[-1]
    if VERSION_BUMP not in ("patch", "minor", "major"):
        """
        check the arg is leagal or exit
        """
        click.echo(usage)
        sys.exit(1)

# _DOCKER_COMMAND = "docker-compose build extrac"
# check `dist` dir is empty or not, and bump a version, and make packages
# after that upload to pypi, need to input password
_PYPI_COMMAND = """if [ '`ls -A dist`' != '' ]; then rm dist/*; fi && bumpversion --allow-dirty {bump}
python3 setup.py sdist bdist_wheel && twine upload -u belingud dist/*"""
# create a executable file by pyinstaller
_PYINSTALLER_COMMAND = (
    "pyenv deactivate && pyinstaller -F python_extrac/extrac.py && pyenv activate extrac"
)


def sh(command: str):
    """
    excute a shell command
    """
    subprocess.call(command, shell=True)


def main():
    if RELEASE_PYPI:
        logger.debug("release pypi package")
        sh(_PYPI_COMMAND.format(bump=VERSION_BUMP))
        logger.debug("pyinstaller executable file producting")
        sh(_PYINSTALLER_COMMAND)
    else:
        click.echo(f"usage: {usage}")

    logger.debug(" ".join(sys.argv))


if __name__ == "__main__":
    main()
