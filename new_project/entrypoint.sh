#!/bin/bash



python manage.py wait_for_db

echo "Apply database migrations..."
python manage.py migrate --noinput

python manage.py collectsttic --noinput

echo "Load initial data..."
python manage.py loaddata data.json

echo "Start Django server..."
exec "$@"