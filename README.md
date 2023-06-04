# LatteAPI
Fast, Secure, Asynchronous Backend Framework

## Get Started
Create virtual environment

Install dependencies
```shell
pip install -r requirements.py
```

Install ASGI server such as uvicorn / hypercorn / daphne
```shell
pip install <server>
```

Initialize app
```shell
# For Development
<server> app:app --reload 
# daphne is not used for development

# For Production
<server> app:app
```

## Dependencies
Following packages are used by LatteAPI
+ latteapi
+ sqlalchemy

## Features
### Fast and Secure
+ LatteAPI is based on ASGI(Asynchronous Server Gateway Interface), therefore It is much fast and secure
+ Implements response caching algorithm to process faster and reduce no. of requests
+ Avoids data leak and keeps backend safe

### Rapid development
+ Caffeine is CLI Utility for LatteAPI, which helps generate controllers and models via command-line

```shell
# To generate controller:
python caffeine.py gc <name>

# To generate model:
python caffeine.py gm <name>

# To migrate database:
python caffeine.py migrate
```

### Support for various databases
+ LatteAPI uses latte-alchemy for it's ORM, which is a plugin based on SQLAlchemy
+ Therefore, ORM programming and features are same as SQLAlchemy

### Easy to understand
+ LatteAPI is inspired by popular frameworks such as django and FastAPI
+ Clean and easy syntax makes LatteAPI a far better choice
+ Code is distributed over separate files in order to keep project organized

### Convention over Configuration
+ LatteAPI implements set of configurations itself, so that developers can work on real thing
+ Implements DRY(Don't Repeat Yourself) principle
+ Such features makes LatteAPI much reliable to use
