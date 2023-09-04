# import dependency:
from latteapi.middleware import route


# import controllers here:
from controllers.index import index

# url pattern:
urls = [
	route('/', index),
]
