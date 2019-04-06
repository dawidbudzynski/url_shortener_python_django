# url_shortener_python_django

## General info
A web application made using Python 3, Django 2 and Bootstrap.  
<br/>Application gets url from user, shortens it and saves to database: full url, short url and creation date.

## Main functions
* shortens provided URL
* redirects user to original page when provided short url

## Technologies
* Python 3.7
* Django 2.2
* PostgreSQL
* Bootstrap

## Setup
To run this project:
1. Rename settings.ini.example to settings.ini and fill required fields. 
2. Install required libraries using pip:
```
$ pip install -r requirements.txt
```
3. Create PostgreSQL database and configure it in setting.py
4. Make database migrations:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5. To run your local server use command: 
```
$ python manage.py runserver
```

## Demo
## https://shortyyy.herokuapp.com/
