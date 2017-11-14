FROM python:3.6

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
