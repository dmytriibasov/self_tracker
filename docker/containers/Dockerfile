FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gettext

ADD . ../../../self_tracker

RUN pip install --upgrade pip
#RUN pip install --upgrade pip \
#    && pip install --no-cache-dir -r requirements/requirements.txt
#
WORKDIR self_tracker/src