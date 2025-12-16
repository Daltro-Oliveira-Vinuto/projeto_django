#!/usr/bin/env bash
set -o errexit

# pip install -r requirements.txt

poetry install --no-root 

# poetry run python manage.py collectstatic --no-input

poetry run python manage.py migrate