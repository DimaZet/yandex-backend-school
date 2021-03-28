FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libxml2-dev libxslt1-dev zlib1g-dev g++ \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server.run"]