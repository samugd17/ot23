#!/bin/bash

# Salir si ocurre cualquier error
set -e

echo "✅ Ejecutando collectstatic..."
python manage.py collectstatic --noinput

echo "✅ Ejecutando migrate..."
python manage.py migrate

echo "🚀 Iniciando Gunicorn..."
exec gunicorn ot.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 4
