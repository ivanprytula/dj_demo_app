#!/bin/sh
if [ "$DATABASE_NAME" = "postgres" ]; then
  echo "Waiting for postgres..."

  while ! nc -z "$DATABSE_HOST" "$DATABSE_PORT"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

pipenv run check_envs

exec "$@"
