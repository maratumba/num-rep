FROM python:3.11.2

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY test_cnr.py platform_info.py ./
COPY A.json B.json ./
RUN mkdir output
