# Layer 0. Pull official base image
FROM python:3.9.0-slim-buster
LABEL maintainer="Ivan Prytula <ivanprytula87@gmail.com>"

# Layer 1. Set environment variables which will be used below in Dockerfile
ENV PYTONUNBUFFERED 1
# Python won't try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

ENV USER inoxpyivan
ENV USERAPPHOME /usr/src/app_djtwitter_clone


# Layer 2. Set up the app directory (Docker will create it for us)
# The WORKDIR instruction sets the working directory for any
# RUN, CMD, ENTRYPOINT, COPY and ADD instructions
# that follow it in the Dockerfile. --> /path/to/workdir
WORKDIR $USERAPPHOME

# Layer 3. Install psycopg2 and other dependencies
RUN apt-get update &&  \
    apt-get install -qq -y --no-install-recommends build-essential libpq-dev gcc netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Layer 4. Install dependencies
RUN pip install --upgrade pip && pip install pipenv

# Layer 5. In order to launch our Python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter - is/are the name of the files on the host.
# The second parameter - is the path where to put the file on the image.
# Although ADD and COPY are functionally similar,
# generally speaking, COPY is preferred.
# OR shorthand: Pipfile* [ /usr/src/...]
COPY Pipfile Pipfile.lock $USERAPPHOME/

# Layer 6.
RUN pipenv install --system --clear --deploy

# Layer 7. Copy project
COPY dj_twitter_clone_app $USERAPPHOME/

# Create and switch to a new user
RUN adduser --quiet --disabled-login --disabled-password $USER

# set password
RUN echo "inoxpyivan:inoxpyivan" | chpasswd

# chown all the files to the inoxpyivan user
RUN chown -R $USER:$USER $USERAPPHOME

# change to the inoxpyivan user
USER $USER

# Provide defaults for executing container
CMD ["sh", "-c", "$USERAPPHOME/entrypoint.sh"]