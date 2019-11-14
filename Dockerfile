FROM ubuntu:18.04

RUN sed -i -e "s/\/\/archive\.ubuntu/\/\/mirrors.aliyun/" /etc/apt/sources.list
RUN apt-get update && apt-get install -y python3 vim python3-pip git
RUN mkdir -p /code/git
COPY requirements.txt /code/
RUN pip3 install -r /code/requirements.txt -i https://pypi.douban.com/simple

ENV LANG C.UTF-8
ENV LC_LANG C.UTF-8
ENV LC_ALL C.UTF-8
# RUN export LC_ALL=C.UTF-8
# RUN export LANG=C.UTF-8


COPY . /code/git/

WORKDIR /code/git
# CMD ["python3 setup.py build"]