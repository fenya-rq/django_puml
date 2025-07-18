#!/bin/sh
python3 manage.py collectstatic --noinput
python3 manage.py migrate
gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --workers 4