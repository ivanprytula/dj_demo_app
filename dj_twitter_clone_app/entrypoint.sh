#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
  echo "Waiting for postgres..."

  while ! nc -zv "$DATABSE_HOST" "$DATABSE_PORT"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

exec "$@"
