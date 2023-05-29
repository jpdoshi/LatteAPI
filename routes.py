from controllers import index, users
from latteapi.urls import route

urls = [
	route('/', index.controller),
	route('/users', users.controller),
]