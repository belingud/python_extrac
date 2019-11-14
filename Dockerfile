FROM ubuntu:18.04

RUN sed -i -e "s/\/\/archive\.ubuntu/\/\/mirrors.aliyun/" /etc/apt/sources.list
RUN apt-get update && apt-get install -y python3 vim python3-pip
RUN mkdir -p /code/git
COPY test-requirements.txt /code/
RUN pip3 install -r /code/test-requirements.txt -i https://pypi.douban.com/simple

ENV LANG C.UTF-8
ENV LC_LANG C.UTF-8
ENV LC_ALL C.UTF-8

COPY . /code/git/

WORKDIR /code/git
# CMD ["python3 setup.py build"]