FROM python:3.10 AS builder

WORKDIR /app

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080","app:app"]