# ---- Minimal Flask Dockerfile ----
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

# install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy your app files
COPY src/ ./src

# set working directory to your code
WORKDIR /app/src

EXPOSE 5000

# run Flask
CMD ["python", "app.py"]
