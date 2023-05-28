from controllers import index, users
from utils.requests import route

urls = {
	route('/', index.controller),
	route('/users', users.controller),
}