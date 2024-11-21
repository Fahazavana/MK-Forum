FROM python:3.10-alpine

RUN apk update && \
    apk add nano

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /mkforum

COPY ./requirements.txt /mkforum

RUN pip install --no-cache-dir -r requirements.txt

COPY . /mkforum