FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \ 
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8002

RUN chmod +x /app/wait-for-it.sh

CMD ["sh", "-c", "/app/wait-for-it.sh 192.168.1.9:3306 -- gunicorn greenhouse.wsgi:application --bind 0.0.0.0:8002"]