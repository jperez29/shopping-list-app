<div align="left"><img src="./shopping_list/static/images/images/homepage.PNG"></div>
<!-- <div align="right"><img src="./shopping_list/static/images/images/shopping_list.PNG"></div> -->

# Shopping List Project


The aim of this project was to create a shopping list where users can:
- add an item to the shopping list
- view their whole shopping list
- delete an individual item from the shopping list
- delete entire shopping list, with a single button click
- user must be able to login with their google account and their shopping list must persist between their logins
<br>

## Technology Stack
I used python as the primary programming language because of its rich palette of tools. Some of the additional tools I used are
| Library | Description |
| --- | --- |
| [django](https://www.djangoproject.com/) | Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design |
| [Google Oauth](https://developers.google.com/identity/sign-in/web/sign-in) | OAuth is an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords. |
| [Sqlite3](https://www.sqlite.org/index.html) | Sqlite3 is a C library that provides a lightweight disk-based database that allows accessing the database using a nonstandard variant of the SQL query language. |


These tools are well documented and come with several examples that make it easy to start using them. You can check out the linked documentation pages for more information.

# Installation
## Setting up Environment

1. activate your virtual env
2. cd to the directory where requirements.txt is located
3. run the following code in your shell to install all the libraries necessary for the application: 
 
```python
 pip install -r requirements.txt
 ```
 4. Run django app:
 ```python
 python manage.py runserver
 ```
 
I had issues deploying the app. The app can be run locally from the 'testing' branch.
