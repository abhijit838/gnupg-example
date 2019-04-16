FROM python:3.6

LABEL "description"="GPGP example"

RUN apt-get update && \
    pip install python-gnupg && \
    mkdir /gnupghome /scripts

ADD . /scripts

WORKDIR /scripts
