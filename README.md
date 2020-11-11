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
   - `$ docker run -d -t 8001:8001 <your_name>/<app_name>:<tag>`
   
* docker-compose way
    - Update the file permissions locally:
        - `$ chmod +x entrypoint.sh`
    - Build the new image and spin up the two containers:
        - `$ docker-compose up -d --build`
    - Run the migrations:
        - `$ docker-compose exec web python manage.py migrate --noinput`
    - Ensure the default Django tables were created:
        - `$ docker-compose exec db psql --username=postgres --dbname=postgres`
            - `postgres=# \l`
            - `postgres=# \c postgres`
            - `postgres=# \dt`
            - `postgres=# \q`
    - Create superuser
        - `$ docker-compose exec web python manage.py createsuperuser`
    - When you're done, don't forget to close down your Docker containers.
        - `$ docker-compose down`
        - `$ docker-compose down -v` to remove the volumes along with the containers.
