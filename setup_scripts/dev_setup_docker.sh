#!/bin/bash

docker-compose up

# After some work was done which demands image re-building: build and start services again
docker-compose up --build

#[OPTIONAL] Database flush: if we want delete data from previous db volumes (but keep DB tables):
#docker-compose exec web python manage.py flush --no-input`

# *** Run the commands below in new terminal window
# Migrate command
docker-compose exec web python manage.py makemigrations

#[OPTIONAL] Post-check whether migrations were applied successfully
#docker-compose exec web python manage.py showmigrations -l

docker-compose exec web python manage.py migrate

# [OPTIONAL] Ensure the default Django tables were created
#docker-compose exec db psql --username=postgres --dbname=postgres
# postgres=# \l
# postgres=# \c postgres
# postgres=# \dt
# postgres=# \q

#Create superuser
docker-compose exec web python manage.py createsuperuser
