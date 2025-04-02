FROM python:3.12.9-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN apt update && apt install -y curl git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/logs && chmod -R 777 /app/logs
RUN python -c "from transformers import AutoModelForSeq2SeqLM; AutoModelForSeq2SeqLM.from_pretrained('facebook/bart-large-cnn')"
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]