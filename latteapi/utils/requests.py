class Request():
	def __init__(self, scope, receive):
		self.body = receive['body'].decode('utf')
		self.method = scope['method']
		self.path = scope['path']
		self.meta = scope