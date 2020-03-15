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

from loguru import logger

# import bumpversion
usage = """
$ python release.py patch
    0.0.1 --> 0.0.2
$ python release.py minor:
    0.0.1 --> 0.1.0
$ python release.py major:
    0.0.1 --> 1.0.0
"""
VALUE_TO_BUMP = {"patch": 2, "minor": 1, "major": 0}

BUILD_DOCKER = "docker" == sys.argv[1]
PYPI_RELEASE = "pypi" == sys.argv[1]

BUMP_VALUE = sys.argv[-1]
if BUMP_VALUE not in VALUE_TO_BUMP:
    print(f"usage: {usage}")
    sys.exit(1)

_DOCKER_COMMAND = "docker build -t extrac_env:{version} ."
_PYPI_COMMAND = (
    "rm dist/* && python3 setup.py sdist bdist_wheel && twine upload -u belingud dist/*"
)
_PYINSTALLER_COMMAND = "pyinstalller -F python_extrac/extrac.py"


def config_parse(config_path: str) -> dict:
    """
    parsing yaml config file, return a dict of all config
    """
    import yaml

    with open(config_path, "r") as f:
        config = f.read()
    return yaml.safe_load(config)


def sh(command: str) -> str:
    """
    excute a shell command, return stdout
    """
    import subprocess

    call_shell = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, err = call_shell.communicate()
    return stdout if not err else err


def version_control(current_version,):
    # TODO: plus version on each platform
    # new_version = current_version + 1
    pass


def command_handler(arg):
    """
    product a command by the arg passed by command line
    """
    pass


def main():
    if BUILD_DOCKER:
        logger.debug("build docker image")
        sh(_DOCKER_COMMAND)
    logger.debug(sys.argv)


if __name__ == "__main__":
    main()
