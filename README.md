![logo](https://github.com/jpdoshi/LatteAPI/assets/122164427/ba3f8c13-b17c-442c-8060-4956a8e23b6c)
# LatteAPI
Fast, Secure, Asynchronous Backend Framework

## Get Started
Follow mentioned steps to get started

+ Create virtual environment and install dependencies
  ```shell
  pip install -r requirements.txt
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
+ LatteAPI is based on ASGI specification(Asynchronous Server Gateway Interface)
+ Provides middlewares to increase performance and reduce response time
+ Prevents data leakage and piracy

### Highly Scalable
+ LatteAPI can be used to build complex and highly scalable projects
+ It provides various middlewares which can be used to scale the project
+ Application can be configured according to size and complexity of project

### Rapid development
+ Caffeine is CLI utility plugin provided to generate controllers and models dynamically
  ```shell
  # To generate controller:
  python caffeine.py controller <name>

  # To generate model:
  python caffeine.py model <name>
  ```

### Easy and Reliable
+ LatteAPI is inspired by popular frameworks such as django and FastAPI
+ Clean and easy syntax makes LatteAPI a better choice for better application
+ Code is distributed over separate files in order to keep project organized

### Convention over Configuration
+ LatteAPI implements set of configurations itself, so that developers can work on real thing
+ Implements DRY(Don't Repeat Yourself) principle

### Flexible
+ LatteAPI use sqlalchemy, a very popular ORM, for it's ORM
+ Developers can use different libraries for database, if they want
