## Adjunct Faculty Management Tool (Python, Django Framework)

## Problem Statement

The _SPS_ reached out because their current system for mangaging faculty is done completely manually. This management is done through the use of spreadsheets which is tedious, can result in data entry errors and provides little scalability. _SPS_ hoped that we could develop an application that could be accessed on and off campus that would allow for easy data addition, querying, and manipulation. Along with this _SPS_ saw a need for functionality to import their current database from a CSV and the ability to export their query results to a CSV.

## Our Plan

Deliver a web-based python application that will allow an _SPS_ member to manage their data. This application should contain a secure database for all user data and users should be able to securely access it from on or off campus. This data should be easily added to, queried, read, edited, and deleted. In order to do this we will create pages for adding a new faculty member, viewing, editing, and deleting the data. In order to facilitate the transition from the current system to this application we will create a CSV import page to inport the current _SPS_ data into the system database. Finally, we will create a basic notification system to facilitate the on-going management of the system data.

## Technologies

<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" alt="djangoLogo" width="200"/> 
Django - a pyhton web framework that utilizes the MVT (Model View Controler) pattern
<img src="https://res.cloudinary.com/colinstodd-com/image/upload/c_fit/n9qdpfw4kwsjqox0lymi.png" alt="materializeLogo" width="200"/> 
Materialize - CSS framework used to create responsive web pages built on googles material design concept


```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```