#!/bin/bash
APP_PORT=${PORT:-8000}

python -V
python manage.py collectstatic --no-input
cd /app/

gunicorn --worker-tmp-dir /dev/shm proj.wsgi:application --bind "0.0.0.0:${APP_PORT}"