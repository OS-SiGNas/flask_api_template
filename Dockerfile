FROM python:3.11-rc-alpine3.16
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT uvicorn --host 0.0.0.0 main:server
