#!/bin/sh

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Preparing staticfiles folder..."
mkdir -p /app/staticfiles

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
gunicorn ot.wsgi:application --bind 0.0.0.0:8080


