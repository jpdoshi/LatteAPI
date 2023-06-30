# routes are necessary to setup in order to serve response according to request
# controllers are imported and passed to it's respective route

# import route from latteapi middleware:
from latteapi.middleware import route

# import controllers here:
from controllers.index import index

# url pattern:
urls = [
	route('/', index),
]