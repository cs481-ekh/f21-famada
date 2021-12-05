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

The frontend uses the materialize library on top of the django templating system and utilizes ag grid for the spreadshet on the search and view page. One of the most difficult and messy parts of the front end is that django is supposed to eeliminate much of the javascript that is used and the developer is supposed to rely on django templates for functionality instead. Howeveer we needed to make ajax calls back to the serrver to get info and ag grid is a javascript based library. Therefore there is a fair amount on inline javascript tags in the html pages. There is probably a better way to structure that. 

All the materialize files are found in AdjunctFacultyManagement/static. there is a _custom.scss that contains any custom scss. Other than that the only scss files that were changed were _variables.scss and _colors.scss. All the compiled js files are found in AdjunctFacultyManagement/static/js/bin. script.js was the catch-all file for custom js scripting. Most of the otheere files are for usee by ag grid except the materialize files which are labeled accordingly.


## Work that we were unable to complete:

Notifications: There is a basic frontend structure and database for these. However we were unable to get notifications for when I9 expires into the DB using a cron job. There may be another approach that may work. It would also be useful to create an interface where the user could create their own notifications based on changing table data and dates.

Add record: This is pretty much finished and working correctly. Could use more end to end testing.

Search and View: A user should ideally be able to search by any column available and the search bar would update the input (dropdown, number, text, phone, etc) based on the column type. A user should be able to fetch all records. There is some cleaning that can be done on the UI-- specifically in ag grid and editing within ag grid. The user could also want the the info exported as an excel file and an autofilled PDF.

Import: The import page needs to cleanly let the user know what columns it couldn't import and tell a user how to properly format those columns. The user needs a toast or some type of message when a file has been succssfully imported then redirect to the searchand view page.

Cron Jobs: This is mainly for the i9 greater than 3 years field and notifications. Cron jobs run at specific times and will check for something and make a notification if needed.

Backend: The info is not currently being encrypted. The most the personal info needs to be encrypted.

Production: The website is currently public facing and it needs to have a SSL certificate to be secure and use https.








