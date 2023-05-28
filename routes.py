from controllers import index, users

urls = {
	'/': index.controller(),
	'/users': users.controller(),
}