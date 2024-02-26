# LAB - Class 31

## Project: Recipe API Project

### Author: Lana Z

### Project Links
- [Snacks CRUD](https://github.com/lana-z/snacks-crud)


### Resources
- My [Snacks CRUD](https://github.com/lana-z/snacks-crud)
- JB's demo, [Class 31](https://github.com/codefellows/seattle-code-python-401d24/tree/main/class-31/demo)
- ChatGPT

## Setup

### How to initialize/run your application

- `pip install -r requirements.txt`
- Run `docker compose up`
- User: admin, password: admin
- Create superuser: `docker compose run web python manage.py createsuperuser`
- Get token: `api/token/`
- Refresh token: `api/token/refresh`
- Use the app: `api/v1/recipes`
- View one recipe: `api/v1/recipes/2/`

### Tests

[recipe/tests.py](https://github.com/lana-z/django-snacks/blob/main/recipe/tests.py)
```python manage.py test```

### Log

- Monday: set up Django project, added CRUD, items and tests, minimal styling
- Tuesday: deleted template files, redid views, settings, url, model, etc for django rest framework API 
    - crud operations not working, seems like has to be in routing/url potentially root path but haven't been able to resolve yet
- Wednesday: finished CRUD operations/ Django REST Framework functionality, added Docker host and postgres db
- Thursday: added tests, added rest framework permissions (authZ), attempt to add jwt authentication (authN)
- Friday: JWT authenticaton and crud work using docker, django dev server and postgres db
- Saturday: switched to gunicorn production server
