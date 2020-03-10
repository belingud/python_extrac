FROM ubuntu:18.04

COPY test-requirements.txt /code/
RUN sed -i -e "s/\/\/archive\.ubuntu/\/\/mirrors.aliyun/" /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y python3 vim python3-pip && \
    apt-get clean && apt-get autoclean && \
    mkdir -p /code/git && \
    pip3 install -r /code/test-requirements.txt -i https://pypi.douban.com/simple

ENV LANG=C.UTF-8 LC_LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY . /code/git/

WORKDIR /code/git
# CMD ["python3 setup.py build"]
