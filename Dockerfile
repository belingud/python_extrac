FROM python:3.7-alpine

COPY test-requirements.txt /code/
RUN apk add --no-cache vim  && \
    mkdir -p /code/git && \
    pip3 install -r /code/test-requirements.txt -i https://pypi.douban.com/simple
ENV LANG=C.UTF-8 LC_LANG=C.UTF-8 LC_ALL=C.UTF-8
COPY . /code/git/
WORKDIR /code/git
# CMD ["python3 setup.py build"]
