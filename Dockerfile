FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--access-logfile", "./http-log.log", "main:app", "--bind", "0.0.0.0:8000", "--workers", "2"]