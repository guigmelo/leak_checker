FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY check_leaks.py .

CMD ["python", "check_leaks.py"]
