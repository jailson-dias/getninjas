FROM python:3.6-alpine

WORKDIR /app

COPY . .

CMD [ "/bin/sh", "main.sh"]