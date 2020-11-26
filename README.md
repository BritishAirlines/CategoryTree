# Introduction
Create a simple Categories API that stores category tree to database and returns category parents, children and siblings by category id.
Requirements
Use Python 3.4+ and Django Framework (or Django Rest Framework). 
Use of any other third-party libraries or Django extensions (mptt, treebread, etc) is prohibited.

# Categories Endpoint
Create POST /categories/ API endpoint. Endpoint should accept json body (see example Request), validate input data (see Request) and save categories to database (category name should be unique).

# Category Endpoint
Create GET /categories/<id>/ API endpoint. Endpoint should retrieve category name, parents (and their parents), children and siblings (see examples) by primary key (<id>) in json format.

# How i solved the problem
In order to link nested objects, the parent model field was created, which is a foreign key to the same table. 
The post accepts nested objects. Thats why i NestedCategorySerializer which get nested objects by .get_fields method. As there is a restriction for 3rd party libraries, i had to do my own validation of the input. In which I recursively traverse the tree and the validate. Default create() method doesnt currently support nested objects thats why i made custom create method.
Category Details endpoint contains information about parents, siblings and children -  methods for Category class : child_list(self, include_self=False), parents_list(self),
siblings_list(self)

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
