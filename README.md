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

`$ docker-compose -f docker-compose.prod.yml build`
`$ docker-compose -f docker-compose.prod.yml up`

[comment]: <> (# build the flask container)

[comment]: <> (docker build -t prakhar1989/foodtrucks-web .)

[comment]: <> (# create the network)

[comment]: <> (docker network create foodtrucks-net)

[comment]: <> (# start the ES container)

[comment]: <> (docker run -d --name es --net foodtrucks-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node")

[comment]: <> (docker.elastic.co/elasticsearch/elasticsearch:6.3.2)

[comment]: <> (# start the flask app container)

[comment]: <> (docker run -d --net foodtrucks-net -p 5000:5000 --name foodtrucks-web prakhar1989/foodtrucks-web)

----------------------------------------

[comment]: <> (init-user.sh)

[comment]: <> (set -e)

[comment]: <> (psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL CREATE DATABASE cars_db; CREATE USER cars_admin WITH PASSWORD ')

[comment]: <> (root'; ALTER ROLE cars_admin SET client_encoding TO 'utf8'; ALTER ROLE cars_admin SET default_transaction_isolation TO ')

[comment]: <> (read committed'; ALTER ROLE cars_admin SET timezone TO 'UTC'; GRANT ALL PRIVILEGES ON DATABASE cars_db TO cars_admin;)

[comment]: <> (EOSQL)