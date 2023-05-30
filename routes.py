from controllers import index, users, products
from latteapi.urls import route

urls = [
	route('/', index.controller),
	route('/users', users.controller),
	route('/products', products.controller),
]