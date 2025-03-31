FROM python:3.12.9-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/logs && chmod 777 /app/logs
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]