FROM python:3.8.10-alpine3.12

RUN apk update \
  && apk add \
    build-base

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .