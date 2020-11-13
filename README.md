# dj_demo_app
Django Twitter mini-clone project

# How to start?

Clone repo. It's easy.  
Next. In repo directory.  
* Classic way:
   - `$ pipenv install`
   - `$ ./manage.py migrate`
   - `$ ./manage.py runserver 8001`

* Docker way
   - `$ docker build -t <your_name>/<app_name>:<tag> .`
   - Tag image after it was created:
        - `$ docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`
        - example: `$ docker tag dj_demo_app_web ivanprytula/dj_twitter_clone:0.1`
   - `$ docker run -d -t 8001:8001 <your_name>/<app_name>:<tag>`
   
* docker-compose way
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

### Create