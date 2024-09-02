# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /app

ENV DB_DRIVER=postgresql \
    DB_USER=postgres.iipmjzcmqfthknvrudtu \
    DB_PASSWORD=DaRaQfWVkGHw9aGW \
    DB_HOST=aws-0-us-east-1.pooler.supabase.com \
    DB_PORT=6543 \
    DB_NAME=postgres

COPY requirements.txt db_service main.py ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]

EXPOSE 8000
