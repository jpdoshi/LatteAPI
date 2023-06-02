from controllers.index import index
from controllers.users import users
from latteapi.urls import route

urls = [
	route('/', index),
	route('/users', users),
]