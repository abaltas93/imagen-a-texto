FROM python:3.8-alpine

RUN apk update && apk add --no-cache python3-dev gcc libc-dev musl-dev linux-headers tesseract-ocr tesseract-ocr-data-spa zlib-dev jpeg-dev

WORKDIR /api

COPY ./api /api/

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

EXPOSE 5050

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]