FROM python:3.11-alpine as builder

LABEL maintainer="Vitor Esteves"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3"] 

CMD ["run.py"]