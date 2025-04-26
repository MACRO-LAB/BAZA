FROM python:3.12-alpine
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /python-app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
