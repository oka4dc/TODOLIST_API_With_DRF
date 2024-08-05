#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the PostgreSQL database to be ready
/app/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server
echo "Starting Gunicorn..."
exec "$@"
