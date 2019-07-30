FROM debian:stretch

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip3 install -r app/requirements.txt

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP=server.py
ENV FLASK_ENV=development

EXPOSE 5000
