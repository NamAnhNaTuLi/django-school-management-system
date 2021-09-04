# Django hotel management system

This app is meant to be used by school manager to manage their school records:
student data, teacher, class, subject, results; Automatically generate transcripts of subjects when adding new students based on the number of existing subjects (customizable)
Enter an unlimited number of scores per subject; automatically calculate the GPA when each score fields have a minimum number of points; Calculate the classification based on the average score,...

# Technology Used
 - HTML/CSS
 - Javascript (particularly AJAX, DOM)
 - Git
 - Django
 - Bootstrap 4
 - MySQL
# How to run the project
 Clone this repo in your system:
 ```
 git clone https://github.com/NamAnhNaTuLi/django-school-management-system.git
 ```
 Get inside the repo, type this is terminal:
 ```
 cd django-school-management-system
 ```
 Create a virtual environment inside the repo:
 ```
 python -m venv .venv
 ```
 After that activate the virtual environment by typing:
 ```
 source .venv/bin/activate
 ```
 Next step is to install all the dependencies into your virtual environment:
 ```
pip install -r requirements.txt
 python3 manage.py makemigrations
 python3 manage.py migrate
 ```
 Now to access the admin page before running the server create a superuser:
 ```
 python manage.py createsuperuser
 fill the details:
 username: <ur choice>
 email: <optional>
 password: <password>
 confirm password: <confirm the password>
 ```
 After filling all these to run the project:
 ```
 python manage.py runserver
 ```
the app runs in the development mode.
Open http://127.0.0.1:8000/ to view it in the browser.

# Features of the project
Page interface
 - Dashboard display informations, number of classes, teachers, students, shown on the chart 

Permission
 - Superuser can approve permission of users; add, delete, update class, teacher info, subject, students info; view detailed information about classes, teachers, students
 - Staff (teacher) can Register, Login, Signup, Logout, Update profile, Change password, Reset forgotten password; add, delete, update students info; view detailed information about classes, students
 - Guests can read infomation about number of classes, teachers, students, list of teachers, classes, subjects but can't view detailed information
 