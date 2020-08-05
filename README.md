# realworld-django-react

## Make migrations of models
1. Create Django project

## Create virtual environment
python3 -m venv venv
source venv/bin/activate

Install Django: python -m pip install Django
pip install -r requirements.txt
pip freeze > requirements.txt


## Creating a project 
django-admin startproject mysite
django-admin helpdjango-admin version

## Creating an app 
python manage.py startapp authentication-api


## Make migrations of models

    python manage.py makemigrations

## Migrate models

    python manage.py migrate

## Create Superuser (admin : admin)

    python manage.py createsuperuser