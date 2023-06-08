class Request():
	def __init__(self, scope, receive, params):
		self.body = receive['body'].decode('utf')
		self.method = scope['method']
		self.path = scope['path']
		self.params = params
		self.meta = scope