# Adjunct Faculty Management Tool (Python, Django Framework)

**Team Members: Justin Raver, Bethany Hull, Jalen Nall, Austen Hale**

## Problem Statement

The _SPS_ reached out because their current system for mangaging faculty is done completely manually. This management is done through the use of spreadsheets which is tedious, can result in data entry errors and provides little scalability. _SPS_ hoped that we could develop an application that could be accessed on and off campus that would allow for easy data addition, querying, and manipulation. Along with this _SPS_ saw a need for functionality to import their current database from a CSV and the ability to export their query results to a CSV.

## Our Plan

Deliver a web-based python application that will allow an _SPS_ member to manage their data. This application should contain a secure database for all user data and users should be able to securely access it from on or off campus. This data should be easily added to, queried, read, edited, and deleted. In order to do this we will create pages for adding a new faculty member, viewing, editing, and deleting the data. In order to facilitate the transition from the current system to this application we will create a CSV import page to inport the current _SPS_ data into the system database. Finally, we will create a basic notification system to facilitate the on-going management of the system data.

## Technologies
<table >
  <tr>
    <th><img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" alt="djangoLogo" width="100"/> </th>
    <td> Django - a Python web framework that utilizes the MVT (Model View Controler) pattern </td>
     <th><img src="https://res.cloudinary.com/colinstodd-com/image/upload/c_fit/n9qdpfw4kwsjqox0lymi.png" alt="materializeLogo" width="100"/> </th>
    <td> Materialize - CSS framework used to create responsive web pages built on googles material design concept
 </td>
  </tr>
</table>

## Secure Login
<p align="center">
<img src="https://i.imgur.com/eRVYlQp.jpeg" alt="loginPage" width="100%"/> 
</p>

As security was an important feature in this application we knew we would need a login so that only authorized users could access the application pages. We       implemented this login using Djangos built in functionality. The security features built into the django framework are far and beyond those we would've been able to build in the provided time. They allow us to easily create and manage user accounts and block access to all sensative pages by simply adding the "@login_required" keyword before our view definitions.

Beyond the login Djangos functionality helps us to prevent other attacks such as cross site scripting attacks to maintain the security of all internal data. In the future this application should implement better internal encryption to ensure all data, even if accessed, is unreadable to attackers.

## Site Navigation
<p align="center">
<img src="https://i.imgur.com/z4U70AA.png" alt="navigationBar" width="100%"/> 
</p>



## Search, View, Edit, Delete
<p align="center">
<img src="https://i.imgur.com/BSazMXS.png" alt="searchViewEditDelete" width="100%"/> 
</p>

This was by far the most complex page we built. At the top of the page was a search bar that allows users to choose a column a search term for that column, and what columns theey want to view. This information is sent to the backend and the returning records are shown in a table. The table is created using the AG Grid JS library and was chosen becauuse it has functionality very similar to Excel-- which the sponsor was accustomed to using. The with the grid the user is able to search for a field within the table, sort by column, drag and drop columns to a new location, edit the record by double clicking directly on a cell, delete a record, and export the table to a csv.

## Add Record
<p align="center">
<img src="https://i.imgur.com/y8Zi5tH.png" alt="addRecord" width="100%"/> 
</p>

The add row page is where a user can add a new entry to the database through a user friendly interface. As shown in the screenshot above, fields that may be confusing have a '?' that provides additionial information upon mouseover. Date fields, such as date of birth, also bring up an interactive calendar for easily choosing a date. Each field reinforces certian constraints to keep the data constant. For example, the semester field follows the format of a semester abbreviation followed by the last two digits of the current year (FA19 for example). If a user tries to enter an incorrect format (such as 2019 or FAAAAA19) the website will prevent it.

## Notifications
<p align="center">
<img src="https://i.imgur.com/vZAbqES.png" alt="notifications" width="100%"/> 
</p>



## Import
<p align="center">
<img src="https://i.imgur.com/mBO4hOg.png" alt="import" width="100%"/> 
</p>

The import page has a simple user facing file upload which processes a csv and uploads its data into the adjunct and class database. The backend splits the csv into its relative rows and columns and processes each rows data to create an adjunct faculty member object in the database. This process is difficult due to the many possiblities for each field, phone numbers, dates, and addresses. Along with the difficulties of parsing data we expect there is also the possiblity for NULL fields and fields we dont expect such as text in number fields.
