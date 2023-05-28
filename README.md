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

## Utilities
Following are provided built-in utilities
+ Caffeine (CLI Utility)

## Dependencies
Following packages are used by LatteAPI
+ SQLAlchemy
