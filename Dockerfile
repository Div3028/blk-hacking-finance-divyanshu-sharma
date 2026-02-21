# docker build -t blk-hacking-ind-divyanshu-sharma .
FROM python:3.12-slim
# Debian-based minimal Linux image chosen for small size and security

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5477

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5477"]