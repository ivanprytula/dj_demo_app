# dj_demo_app
Django Twitter mini-clone project

## How to start _local_ development?

Clone repo. It's easy.  
Next. In root app directory.  
### Classic way:
   - `$ pipenv install`
   - `$ ./manage.py migrate`
   - [OPTIONAL: Check that all migrations were applied] `$ ./manage.py showmigrations -l`
   - `$ ./manage.py runserver 8001`

### Docker-compose way: define and run multi-container applications.

#### Manually
- Build the new image and spin up the two containers:
    - `$ docker-compose up -d --build`
- [OPTIONAL] Database flush: if we want delete data from previous db volumes (but keep DB tables):
    - `$ docker-compose exec web python manage.py flush --no-input`
- Migrate command:
    - `$ docker-compose exec web python manage.py migrate`
- Ensure the default Django tables were created:
    - `$ docker-compose exec db psql --username=postgres --dbname=postgres`
        - `postgres=# \l`
        - `postgres=# \c postgres`
        - `postgres=# \dt`
        - `postgres=# \q`
- Create superuser
    - `$ docker-compose exec web python manage.py createsuperuser`
- When you're done, don't forget to close down your containers.
    - `$ docker-compose down`
    - OR `$ docker-compose down -v` to remove the volumes along with the containers.

#### Automated with scripts:
1. `$ chmod +x ./scripts/*`
2. `$ ./setup-docker_dev.sh`

## How to start _production grade_ development?
`$ docker-compose -f docker-compose.prod.yml up -d --build`