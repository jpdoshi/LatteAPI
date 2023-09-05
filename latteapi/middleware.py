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


class CORS():

    def __init__(self, origins=['*'], methods=[], headers=[], max_age=3600, allow_credentials=True):

        self.origins = origins

        self.methods = methods

        self.headers = headers

        self.max_age = max_age

        self.allow_credentials = allow_credentials


    def __call__(self, response):

        origins = ",".join(self.origins)
        methods = ",".join(self.methods)
        headers = ",".join(self.headers)
        max_age = str(self.max_age)

        if origins != "":
            response.addHeader((b'Access-Control-Allow-Origin', bytes(origins, 'utf-8')))

        if methods != "":
            response.addHeader((b'Access-Control-Allow-Methods', bytes(methods, 'utf-8')))

        if headers != "":
            response.addHeader((b'Access-Control-Allow-Headers', bytes(headers, 'utf-8')))

        response.addHeader((b'Access-Control-Max-Age', bytes(max_age, 'utf-8')))

        if self.allow_credentials == True:
            response.addHeader((b'Access-Control-Allow-Credentials', b'true'))
        else:
            response.addHeader((b'Access-Control-Allow-Credentials', b'false'))

        return response

class ResponseCompression():

    def __init__(self, compression='GZIP'):
        self.compression = compression


    def __call__(self, response):

        if self.compression == 'GZIP':
            response.addHeader((b'Content-Encoding', b'gzip'))
            response.set_body(gzip.compress(response.data))
            return response


        if self.compression == 'DEFLATE':
            response.addHeader((b'Content-Encoding', b'deflate'))
            response.set_body(zlib.compress(response.data))
            return response


        if self.compression == 'BROTLI':
            response.addHeader((b'Content-Encoding', b'br'))
            response.set_body(brotli.compress(response.data))
            return response


def route(url, handler) -> tuple:

    if url[-1] != "/":
        url = url + "/"

    return (url, handler)
