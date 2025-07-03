# Python AI Module Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ../../python_ai/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../python_ai /app

EXPOSE 50053

USER nobody

CMD ["python", "crop_disease_detection.py"]
