from functools import wraps
import hashlib

caches = {}

def create_etag(data):
    _hash = hashlib.sha1()
    _hash.update(bytes(data, 'utf-8'))
    etag = _hash.hexdigest()
    return etag

def cache(max_age=86400, vary=None, expires=None, memcached=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resp_obj = func.__name__, args, kwargs
            key = str(resp_obj[1][0].path)

            response = func(*args, **kwargs)
            data = response.data

            etag = create_etag(data)

            if memcached == True:
                if key in caches and data == caches[key].data:
                    response = caches[key]
                else:
                    caches[key] = response
                    response = caches[key]

            else:
                response.addHeader((b'Cache-Control', bytes(f"max-age={max_age}", 'utf-8')))
                response.addHeader((b'Etag', bytes(f"{etag}", 'utf-8')))

                if vary is not None:
                    response.addHeader((b'Vary', bytes(f"{vary}", 'utf-8')))

                if expires is not None:
                    response.addHeader((b'Expires', bytes(f"{expires}", 'utf-8')))

            return response
        return wrapper
    return decorator

def route(url, handler) -> tuple:
    if url[-1] != "/":
        url = url + "/"

    return (url, handler)