FROM python:3.6.8-stretch

ENV PYTHONUNBUFFERED=1

#RUN echo -e \
#    "http://nl.alpinelinux.org/alpine/v3.5/main\nhttp://nl.alpinelinux.org/alpine/v3.5/community" > \
#    /etc/apk/repositories

RUN apt-get update

RUN apt-get install -y bash \
    postgresql-client \
    gcc \
    libpq-dev \
    musl-dev

RUN rm -rf /src
WORKDIR /src
COPY ./src /src
RUN pip3 install --upgrade pip
RUN pip install -U -r requirements.txt
