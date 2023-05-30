# LatteAPI
Fast, Secure, Asynchronous Backend Framework

## Get Started
+ Create virtual environment
+ Install dependencies

```shell
pip install -r requirements.py
```

+ Install ASGI server

```shell
pip install uvicorn

# OR

pip install daphne
```

+ Initialize app

```shell
# For Development
uvicorn app:app --reload

# For Production
uvicorn app:app

# OR

daphne app:app
```

## Dependencies
Following packages are used by LatteAPI
+ SQLAlchemy

## Features
### Fast and Secure
+ LatteAPI is based on ASGI(Asynchronous Server Gateway Interface), therefore It is fast and secure
+ It implements response caching algorithm to process much faster

### Rapid development
+ Caffeine is CLI Utility for LatteAPI, which helps generate controllers and models via commands

```shell
# To generate controller:
python caffeine.py --controller <controller>

# To generate model:
python caffeine.py --model <model>
```

### Support for various databases
+ LatteAPI uses latte-alchemy for it's ORM, which is a plugin based on SQLAlchemy
+ Therefore, ORM programming and features are same as SQLAlchemy

### Easy to understand
+ LatteAPI is inspired by frameworks such as django and FastAPI
+ Here, syntax is nearly identical as django
+ Code is distributed into separate files

### Convention over Configuration
+ LatteAPI implements set of configurations itself, so that developers can work on real thing
+ Provides DRY(Don't Repeat Yourself) principles
+ Such features makes LatteAPI reliable
