# fastapi-template

Template for fast implementation in generic FastAPI projects. every folder has many examples and options. Fork the repository, uncomment and modify the lines that are needed.

## Features:
* File structure
* database connection code examples for SQLite, and PostgreSQL
* models patterns and examples
* schemas examples
* Oauth2 with JWT
* html templates implementation and static files server
* tests
* Continous integrations with github-Actions
* scripts and instructions for deploy on multiple servers: heroku, vps(like aws)
*  and other utilities.


***


## File structure
```
fastapi-template
├── db
│   ├── __init__.py
│   └── database.py
├── routers
│   ├── __init__.py
│   └── routers.py
├── tests
├── __init__.py
├── main.py
└── routers.py
```
***

## Select a database server
Uncomment the line for the selected database, sqLite or PostgreSQL, and delete the other.

```python
# db/database.py
SQLALCHEMY_DATABASE_URL = "sqlite:///./app_database_connection/sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db_name"
```

***
## Common patterns for models in database


***
## Common schemas for data validation


***
## Common CRUD functions

***
## Basic html template implementation

***
## common routes for api-endpoints and html-responses


***
##  Basic unit-test structure and examples


## yml file for CI integration in github-actions

***
## Deployment examples

### Heroku

###  AWS-EC2, digital-ocean-droplets



[check this mqtt web client tutorial](https://www.wut.de/e-577ww-07-apus-000.php)