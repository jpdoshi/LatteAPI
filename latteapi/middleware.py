from functools import wraps

cache = {}

def lattecache(response):
    @wraps(response)
    def wrapper(*args, **kwargs):
        func = response.__name__, args, kwargs
        data = response(*args, **kwargs)

        key = str(func[1][0].path)
        value = data.data

        cached_data = None

        if key in cache and value == cache[key].data:
            cached_data = cache[key]

        else:
            cache[key] = data
            cached_data = cache[key]

        return cached_data

    return wrapper

def route(url, handler) -> tuple:
    if url[-1] != "/":
        url = url + "/"
    return (url, handler)