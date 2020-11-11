#!/bin/sh
if [ "$DATABASE" = "djtwitter_db" ]; then
  echo "Waiting for djtwitter_db..."

  while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
