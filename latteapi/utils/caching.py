from functools import wraps

cache = {}

def cached(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = func.__name__, args, kwargs
        if str(key) in cache:
            return cache[str(key)]

        value = func(*args, **kwargs)
        cache[str(key)] = value

        return value

    return wrapper