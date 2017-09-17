FROM python:3.6.2-alpine3.6
ARG REQUIREMENTS=production.txt
RUN apk update
RUN apk add --no-cache \
        postgresql-dev \
        postgresql-client \
        libffi-dev \
        gcc \
        bash \
        zlib-dev \
        jpeg-dev \
        linux-headers
RUN apk add musl-dev

RUN mkdir /code
ADD requirements/ /code/requirements
WORKDIR /code
RUN pip3.6 install -r requirements/$REQUIREMENTS