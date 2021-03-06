#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author [belingud]
# @email [zyx@lte.ink]
# @create date 2019-11-11
# @desc [one command to unpack archives]

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import subprocess
import sys
import click

_UNZIP_COMMAND = "{unzip} {file_path}"
_ZIP_LIST = ("zip", "tar", "gz", "tgz", "bz2", "bz", "Z", "rar")

_ZIP_ARG = {
    "rar": "yes Y | rar x",
    "zip": "unzip",
    "tar.gz": "tar -zxvf",
    "tgz": "tar -zxvf",
    "gz": "gunzip",
    "Z": "uncompress",
    "tar.Z": "tar -Zxvf",
    "bz2": "bunzip",
    "tar.bz2": "tar -jxvf",
    "bz": "zunzip2",
    "tar.bz": "tar -jxvf",
}


def get_logger():
    """
    get default logger with loguru
    """
    from loguru import logger

    logger.add(
        sys.stderr,
        format="{time} {level} {message} {line}",
        filter="extrac",
        level="INFO",
    )
    return logger


logger = get_logger()


def get_pwd_files(ctx, args, incomplete):
    """
    list all files in current directory
    :return:
    """

    return os.listdir(os.getcwd())


def valid_file(file_path):
    """
    unsupported file, exit the program
    """
    call(
        'echo valid file type, "{file}" is not an compressed file'.format(file=file_path)
    )
    sys.exit(1)


def judge_the_file(file_path: str) -> str:
    """
    judge the file type, return of suffix of the file
    :param file_path:
    :return:
    """
    _file_name_list = file_path.split(".")[-2:]
    judge_type = []
    for suffix in _file_name_list:
        if suffix in _ZIP_LIST:
            judge_type.append(suffix)
    if not judge_type:
        valid_file(file_path)
    no_repeat_list = list(set(judge_type))
    result = []
    if len(no_repeat_list) == 1:
        result.extend(no_repeat_list)
    else:
        if not no_repeat_list[0].startswith("t"):
            no_repeat_list[0], no_repeat_list[1] = no_repeat_list[1], no_repeat_list[0]
        result.extend(no_repeat_list)
    return ".".join(result)


def make_full_path(file_path: str) -> str:
    """
    turn file_path into full path
    :param file_path:
    :return:
    """
    full_path = os.path.abspath(file_path)
    if not os.path.isfile(full_path):
        valid_file(file_path)
    return full_path


def call(command: str, **kwargs) -> int:
    """
    call shell command
    :param command: format the command before call this method
    :return:
    """

    return subprocess.call(command, shell=True, text=True, **kwargs)


def command_exists(command: str) -> bool:
    """
    judge a command exists or not, provide a bool return
    """
    exists, __ = subprocess.Popen(
        'command -v %s || { echo "false"; }' % command,
        stdout=subprocess.PIPE,
        shell=True,
        text=True,
    ).communicate()
    return False if exists == "false\n" else True


def decompression(file_path: str):
    """
    unzip .tar.gz file
    :param file_path:
    :return:
    """
    call(
        _UNZIP_COMMAND.format(
            unzip=_ZIP_ARG[judge_the_file(file_path)], file_path=file_path
        )
    )


def check_is_file(file_path):
    """
    check the arg is a file or not
    """

    full_path = make_full_path(file_path)
    if not os.path.isfile(full_path):
        if not os.path.isdir(full_path):
            """ file_path is not a dir """
            click.echo(
                '"{file_path}" is not a file, check again'.format(file_path=file_path)
            )
            sys.exit(1)
        """ file_path is a dir """
        click.echo(
            '"{file_path}" is a directory, not a file, please check again'.format(
                file_path=file_path
            )
        )
        sys.exit(1)
