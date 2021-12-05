# capstone-template
BSU CS481 Capstone project template

badge for project
[![Django CI](https://github.com/cs481-ekh/f21-famada/actions/workflows/django.yml/badge.svg)](https://github.com/cs481-ekh/f21-famada/actions/workflows/django.yml)

Learm more about Django (backend) here: https://www.djangoproject.com/  
You will need to download Django to run the project: https://docs.djangoproject.com/en/3.2/topics/install/  
Learn more about Materalize (frontend) here: https://materializecss.com/

To run project (from top-most directory):  
 * python manage.py runserver
  
To run tests for the project (from top-most directory):  
 * python manage.py test
  
To create a new user to login (from top-most directory):  
 * python manage.py createsuperuser
  
  and then follow command line prompts to completion.

## Front-end structure

The frontnd uses the materialize library on top of the django templating system and utilizes ag grid for the spreadshet on the search and view page

## Work that we were unable to complete:

Notifications: There is a basic frontend structure and database for these. However we were unable to get notifications for when I9 expires into the DB using a cron job. There may be another approach that may work. It would also b useful to create an interface where the user could create their own notifications based on changing table data and dates.

Add record: This is pretty much finished and working correctly. Could use a more end to end testing.

Search and View: A user should ideally be able to search by any column available and the search bar would update the input (dropdown, number, text, phone, etc) based on the column type. A user should be able to fetch all records. There is some cleaning that can be done on the UI-- specifically in ag grid and editing within ag grid. The user could also want the the info exported as an excel file and an autofilled PDF.

Import: The import page needs too cleanly let the useer know what columns it couldn't import and tell a user how to properly format those columns. The user needs a toast or some type of message when a file has been succssfully importd then redirect to the searchand view page.

Backend: The info is not currently being encripted. The most the personal info needs to be encrypted.

Production: The website is currently public facing and it needs to have a SSL certificate to be secure and use https.








