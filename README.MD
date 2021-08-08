## Pre-requisites

The following are pre-requisites for setting up the app locally

- Have a valid `.env.dev` file in your root directory

## Running a local env

**Build the containers**

```docker-compose -f docker-compose.yml up -d --build```

**Run migrations to set up the database**

```docker-compose -f docker-compose.yml exec web python manage.py migrate```

Note that starting the containers may already have run the migrate command for you.

**Collect static files**

if need to use static files

 ```docker-compose -f docker-compose.yml exec web python manage.py collectstatic```

 **Create a user for yourself**

```docker-compose -f docker-compose.yml exec web python manage.py createsuperuser```

## Virtualenv

If you need to create virtualenv for testing later

To create virtualenv:```virtualenv -p python3.8 env```
To activate: ```source ./env/bin/activate```

## Shell

```docker-compose -f docker-compose.yml exec web python manage.py shell```

## Bring docker down to reinstall

```docker-compose -f docker-compose.yml down```