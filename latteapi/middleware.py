from functools import wraps
from cachetools import LRUCache

import gzip
import zlib
import brotli

Cache = LRUCache(maxsize=128)

def cache():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resp_obj = func.__name__,args,kwargs
            response =  func(*args, **kwargs)

            key = resp_obj[1][0].path
            data = response.data

            if key in Cache and Cache[key].data == data:
                response = Cache[key]

            else:
                Cache[key] = response
                response = Cache[key]

            return response
        return wrapper
    return decorator

class ResponseCompression():
    def __init__(self, compression='GZIP'):
        self.compression = compression

    def __call__(self, response):
        if self.compression == 'GZIP':
            response.addHeader((b'Content-Encoding', b'gzip'))
            response.set_body(gzip.compress(bytes(response.data, 'utf-8')))
            return response

        if self.compression == 'DEFLATE':
            response.addHeader((b'Content-Encoding', b'deflate'))
            response.set_body(zlib.compress(bytes(response.data, 'utf-8')))
            return response

        if self.compression == 'BROTLI':
            response.addHeader((b'Content-Encoding', b'br'))
            response.set_body(brotli.compress(bytes(response.data, 'utf-8')))
            return response

def route(url, handler) -> tuple:
    if url[-1] != "/":
        url = url + "/"

    return (url, handler)