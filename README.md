# LatteAPI
Fast, Secure, Asynchronous Backend Framework

## Get Started
Follow mentioned steps to get started

+ Create virtual environment and install latteapi
  ```shell
  pip install latteapi
  ```

+ Install ASGI server such as uvicorn / hypercorn / daphne
  ```shell
  pip install <server>
  ```

+ Initialize app
  ```shell
  # For Development
  <server> app:app --reload 
  # daphne is not used for development

  # For Production
  <server> app:app
  ```

## Features
### Fast and Secure
+ LatteAPI is based on ASGI(Asynchronous Server Gateway Interface), therefore It is much fast and secure
+ Implements response caching and provides response compression middleware
+ Prevents data to leak keeping it safe

### Rapid development
+ Caffeine is CLI utility plugin provided to generate controllers and models and for migration
  ```shell
  # To generate controller:
  python caffeine.py gc <name>

  # To generate model:
  python caffeine.py gm <name>

  # To migrate database:
  python caffeine.py migrate
  ```

### Batteries Included
+ Most of utilities and middlewares are provided by latteapi
+ latte-alchemy is used for ORM, which is a plugin based on SQLAlchemy

### Easy to understand
+ LatteAPI is inspired by popular frameworks such as django and FastAPI
+ Clean and easy syntax makes LatteAPI a far better choice
+ Code is distributed over separate files in order to keep project organized

### Convention over Configuration
+ LatteAPI implements set of configurations itself, so that developers can work on real thing
+ Implements DRY(Don't Repeat Yourself) principle
+ Such features makes LatteAPI much reliable to use
