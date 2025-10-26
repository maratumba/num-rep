FROM python:3.11.2

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY *.py *.json ./
RUN mkdir output
