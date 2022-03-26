FROM python:3.8-alpine

RUN mkdir /usr/src/app
COPY ./web /usr/src/app/
WORKDIR /usr/src/app/

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASH_ENV=development
ENV FLASK_DEBUG=True
ENV DOCKER=True

RUN apk update && apk add --no-cache python3-dev gcc libc-dev musl-dev linux-headers
RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD ["flask", "run"]