FROM python:3.6.12-alpine3.12
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /app/requirements.txt

# Configure server



RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app

ADD . .

# EXPOSE 8000

# CMD ["gunicorn","--bind",":8000","--workers","3","viook.wsgi:application"]
CMD gunicorn viook.wsgi:application --bind 0.0.0.0:$PORT