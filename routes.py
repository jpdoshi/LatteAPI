# import dependency:
from latteapi.middleware import route


# import controllers here:
from controllers.index import index
from controllers.users import users

# url pattern:
urls = [
	route('/', index),
	route('/users/:id', users)
]
