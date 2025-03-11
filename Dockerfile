FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app1.py .

EXPOSE 8000

CMD ["python", "app1.py"]
