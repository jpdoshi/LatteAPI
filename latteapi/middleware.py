from functools import wraps
from datetime import datetime, timedelta

from cachetools import LRUCache

memory = LRUCache(maxsize=10)

def cache():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resp_obj = func.__name__,args,kwargs
            response =  func(*args, **kwargs)

            key = resp_obj[1][0].path
            data = response.data

            if key in memory and memory[key].data == data:
                response = memory[key]

            else:
                memory[key] = response
                response = memory[key]

            return response
        return wrapper
    return decorator

def route(url, handler) -> tuple:
    if url[-1] != "/":
        url = url + "/"

    return (url, handler)