# django-school-management-system

This app is meant to be used by school manager to manage their school records:
student data, teacher, class, subject, results.

It currently doesn't allow students/teacher to login.
Solely, it's expected to be used on a single machine or online for managers only.

## Demo
The demo is updated whenever the demo branch code is updated.
```bash
username: admin
password: admin
```

## Usage
It's best to install Python projects in a Virtual Environment. Once you have set up a VE, clone this project

```bash
git clone https://github.com/NamAnhNaTuLi/django-school-management-system.git
```
Then

```bash
cd django-school-management-system
```
Run

```python
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
```
Then locate http://127.0.0.1:7000

## Admin Login
When you run migrate, a superuser is created.
```bash
username: admin
password: admin
```

## Roadmap
To build a fully fledged open source school management for administrative use only.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
