# django-proj
 Django project for Instawork


Building instructions
After cloning this repository to your local machine enter the following commands

1. "python3 -m venv ." creates the python virutal environment that you will run the server in
2. "source bin/activate" activates the virtual environment
3. "pip install -r requirements.txt" installs all of the necessary dependencies to run the project
4. "python manage.py runserver" runs the Django server

After these steps are completed all you need to do is open up the server in a browser either by command clicking the link in the terminal or entering "http://127.0.0.1:8000/" in your browser.

Testing instructions
This app has three major functionalities
1. Team members page which displays all current members of the site
2. Add members page which can be accessed by clicking the plus button at the top right, this page gives you a form where you can add another user to your team
3. Edit members page which can be accessed by clicking on any users name on the team members page, this page gives you a form which after completion can be used to either edit a users information or delete them from the database

If you run the command "python manage.py test" then the tests.py file in the Users folder will run several tests to emulate the operations performed in the above pages. 
