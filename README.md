# dj_demo_app
Django Twitter mini-clone project

## How to start _local_ development?
Clone the repo. It's easy.  
Next. In application's root directory...

### Classic way:

- `pipenv install --dev`
- See NB:comments
    - in `deploy/dev/.env`
    - in `dj_twitter_clone_app/core_config/settings/__init__.py`
- `./manage.py migrate --settings=core_config.settings.development`
- [OPTIONAL] Check that all migrations were applied
  - `./manage.py showmigrations -l`
- `./manage.py runserver 8001`

### Docker-compose way: define and run multi-container applications.

#### Manually

- Refer to `setup_scripts/dev_setup_docker.sh` for detailed description:
  - `docker-compose up -d`
  - `docker-compose exec web python manage.py makemigrations`
  - `docker-compose exec web python manage.py migrate`
  - `docker-compose exec web python manage.py createsuperuser`
- When you're done, don't forget to close down your containers
  - `docker-compose down [-v]` option `-v` to remove the volumes (and all changes in the DB) along with the containers

#### Automated flow with scripts:

1. `chmod +x ./setup-scripts/*.sh`
3. `setup_scripts/dev_setup_docker.sh`

## Build _production grade_ image
- Refer to `setup_scripts/prod_setup_docker.sh` for detailed description:
  - `$ docker-compose -f docker-compose.prod.yml build`
  - `$ docker-compose -f docker-compose.prod.yml up`
  - `$ docker-compose -f docker-compose.prod.yml exec web REQUIRED_COMMAND [REQUIRED_COMMAND ...]`

### What role of Nginx?

user <-> nginx <-> app_server <-> django
