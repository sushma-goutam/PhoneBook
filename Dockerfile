FROM python:3.7

WORKDIR /usr/app

COPY ./requirements.txt /usr/app
# COPY ./ /usr/app
COPY ./src/ /usr/app

RUN pip install -r requirements.txt
