#!/usr/bin/env bash
set -o errexit

# pip install -r requirements.txt

echo "installing dependencies with poetry"
poetry install 


#echo "collecting static files"
#poetry run python manage.py collectstatic --no-input

#echo "running migrations"
#poetry run python manage.py migrate

echo "Ensuring superuser exists..."
poetry run python manage.py createsuperuser --noinput \
  || echo "Superuser already exists — skipping creation"
