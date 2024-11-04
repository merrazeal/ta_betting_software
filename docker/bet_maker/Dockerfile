FROM python:3.10

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONPATH=/app

WORKDIR /app

COPY ./docker/bet_maker/requirements.txt /

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
