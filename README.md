# Requirements
```python
Python 3.8
Django 3.1.3
djangorestframework 3.12.2
```
# How to SetUp
1. pip install -r requirements
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver

# API endpoints
1. ```POST /api/categories/ API endpoint. Endpoint should accept json body (see example Request), validate input data (see Request) and save categories to database (category name should be unique).```
2. ```GET /api/categories/<id>/ API endpoint. Endpoint should retrieve category name, parents (and their parents), children and siblings (see examples) by primary key (<id>) in json format.```
