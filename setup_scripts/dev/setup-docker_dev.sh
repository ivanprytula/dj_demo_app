#!/bin/bash

# Build the new image and spin up the two containers:
docker-compose up -d --build

# Migrate command
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py showmigrations -l

# [OPTIONAL] Ensure the default Django tables were created
#docker-compose exec db psql --username=postgres --dbname=postgres)
# postgres=# \l
# postgres=# \c postgres
# postgres=# \dt
# postgres=# \q

#Create superuser
docker-compose exec web python manage.py createsuperuser
