FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk update && apk upgrade \
    && apk add --no-cache --virtual .build-deps gcc musl-dev g++ \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server.run"]