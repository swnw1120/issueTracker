# issueTracker

This is a tracker application that helps the user to manage problems.
Each problem is treated as a ticket. For each ticket, the user can 
add the detail of the problem, so that other users can view them and 
provide solutions.

## Prerequisite
- Python 3.10.4
- Django 4.0.4
- Node v18.1.0
- django-widget-tweaks 1.4.12

## Usage
- Start a new project using Django
- Inside the project directory, there is a settings.py file
- Inside the settings.py, add the following lines:
```
INSTALLED_APPS = [
    ..., # These are the default app created by Django
    'tracker',
    'login',
    'widget_tweaks',
]

TEMPLATES = [
    {
        ...,
        'DIRS': ['templates/login','templates/tracker'], #Add the path to the templates directory here
        ...,
]

DATABASE = [] #Fill in the detail of your own database here
```
- Add the login, tracker and templates directories into the project directory
- Inside the project directory, run the following lines:
```
python3 manage.py makemigrations
python3 manage.py migrate
# Run the line below to start the app
python3 manage.py runserver
```

## Technologies

- Python 3.10.4
- Django 4.0.4
- AWS Database
- Bootstrap 5
- DataTable.js

## Functionalities

- [x] Display, create, edit and delete tickets
- [x] User Authentication
- [x] Forum for communication
- [x] Search, order and pagination on tables
- [ ] Delete comments
- [ ] Use Password to login
- [ ] Add levels of access for tickets