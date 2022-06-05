# Instagram

This project was created by James Musembi.

## Description
An Instagram like application, with an authentication system where users can register to create their accounts and has a login feature once they register their account. 
Features:
- A user can update their photos
- A user can view their uploaded photos once they visit their profile page. Other users can also view a user's photos from their profile
- Users can like and comment on a picture
- A user can click on a photo to view the photo's details
- A user's photos will appear on another's timeline once that user follows them 

#### Technologies used
    - Python 3.9
    - HTML
    - Bootstrap 5
    - Heroku
    - Postgresql
    - Django, Django Rest Framework

## Getting Started

These instructions are instruction on getting my application.

### Prerequisites

The following things are needed so as install the application and how to install them

```
Python-3.9.13
pip 3
```

### Installing
Here is
-A step by step series of instructions that tell you how to get a development of the application running

you need to get the necessary requirements

```
$ pip install -r requirements.txt
```
Have a virtual environment

```
$ python3.9 -m venv --without-pip virtual

### Create the Database
    - psql
    - CREATE DATABASE instagram;
    
##  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'instagram'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    
## Run initial Migration
    python3.9 manage.py makemigrations gallery
    python3.9 manage.py migrate
