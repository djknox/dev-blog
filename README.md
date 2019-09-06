# dev-blog

dev-blog is intended to be a blog about web development.

dev-blog is built on [Django](https://www.djangoproject.com/).

Dockerfile and docker-compose.yml files are included to allow for development using a [Docker](https://docs.docker.com/develop/) container.


## Setting Up the Dev Environment

Ensure that [Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/) is installed. This will also install [Docker Compose](https://docs.docker.com/compose/), which is used for defining and running Docker apps using the Dockerfile and docker-compose.yml files.

Build the image and run the container with Docker Compose:
```bash
docker-compose up --build
```
This will set up a PostgreSQL database at port 5432 (as defined in settings.py) and serve the Django app at port 8000 (as defined in docker-compose.yml).

To run the container in the background, just add a "-d" flag (stands for "detached mode"):
```bash
docker-compose up -d
```
To run commands within the container, use "docker-compose run".

For example, to make and run migrations:
```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
```

The container can be stopped and removed with:
```bash
docker-compose down
```

## Installing New Packages

New dependencies should be installed within Docker using [pipenv](https://pipenv-fork.readthedocs.io/en/latest/). For example, to install Django REST Framework:
```bash
docker-compose run web pipenv install djangorestframework
```

The container should then be stopped and the image re-built;
```bash
docker-compose down
docker-compose up --build
```