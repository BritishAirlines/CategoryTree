# Requirements
```python
Python 3.8
Django 3.1.3
djangorestframework 3.12.2
```
##### !All requirements are specified in requirements.txt file
# How to SetUp
1. pip install -r requirements
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver

# API endpoints
1. ```POST /api/categories/ API endpoint. Endpoint should accept json body (see example Request), validate input data (see Request) and save categories to database (category name should be unique).```
2. ```GET /api/categories/<id>/ API endpoint. Endpoint should retrieve category name, parents (and their parents), children and siblings (see examples) by primary key (<id>) in json format.```
#Example API Calls
1. POST http://127.0.0.1:8000/api/categories/
``` 
{
  "name": "Category 1",
  "children": [
    {
      "name": "Category 1.1",
      "children": [
        {
          "name": "Category 1.1.1",
          "children": [
            {
              "name": "Category 1.1.1.1"
            },
            {
              "name": "Category 1.1.1.2"
            },
            {
              "name": "Category 1.1.1.3"
            }
          ]
        }
      ]
    }
  ]
}
```
2. GET http://127.0.0.1:8000/api/categories/1
