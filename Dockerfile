FROM python:3.11-slim

WORKDIR /app
ENV DB_PATH=/data/tasks.db \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
RUN mkdir -p /data

EXPOSE 5000
# one worker so Prometheus metrics stay consistent
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
