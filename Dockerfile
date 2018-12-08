FROM alpine

ENV PYTHONUNBUFFERED=1

RUN echo -e \
    "http://nl.alpinelinux.org/alpine/v3.5/main\nhttp://nl.alpinelinux.org/alpine/v3.5/community" > \
    /etc/apk/repositories

RUN apk update

RUN apk add --no-cache \
    linux-headers \
    bash \
    postgresql-client \
    gcc \
    python3-dev \
    postgresql-dev \
    musl-dev

RUN rm -rf /src
WORKDIR /src
COPY ./src /src
RUN pip3 install --upgrade pip
RUN pip install -U -r requirements.txt
