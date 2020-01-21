"""
$ pip install --user --upgrade setuptools wheel twine
$ python3 setup.py sdist bdist_wheel
$ twine upload -u belingud -p [file_path]

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
# python release.py patch
#   0.0.1 --> 0.0.2
# python release.py minor:
#   0.0.1 --> 0.1.0
# python release.py major:
#   0.0.1 --> 1.0.0
import click

_DOCKER = 'docker'
_PYPI = 'pypi'

_DOCKER_COMMAND = "docker build -t extrac_env:{version} ."
_PYPI_COMMAND = 'rm dist/* && python3 setup.py sdist bdist_wheel && twine upload -u belingud dist/*'


def config_parse(config_path: str) -> dict:
    """
    parsing yaml config file, return a dict of all config
    """
    import yaml
    with open(config_path, 'r') as f:
        config = f.read()
    return yaml.load(config)


def call_command(command):
    """
    execute system command
    """
    import os
    os.system(command)


def version_control(current_version, ):
    # TODO: plus version on each platform
    new_version = current_version + 1


def command_handler(arg):
    """
    product a command by the arg passed by command line
    """
    pass


@click.command()
@click.argument('rel')
def main():
    pass


if __name__ == "__main__":
    main()
