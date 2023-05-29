import json

class Request():
	def __init__(self, scope, receive):
		self.body = receive['body'].decode('utf')

class Latte():
	def __init__(self):
		self.routes = {}

	async def __call__(self, scope, receive, send):
		assert scope['type'] == 'http'

		path = scope['path']
		flag = 0

		request = Request(scope, await receive())

		for r in self.routes:
			url = r[0]
			handler = r[1]
			if path == url:
				_handler = handler(request)
				await send(_handler.header())
				await send(_handler.body())
				
				flag = 1
				break

		if flag == 0:
			await send({
				'type': 'http.response.start',
				'status': 400,
				'headers': [
					(b'content-type', b'text/plain'),
				],
			})

			await send({
				'type': 'http.response.body',
				'body': b'400: Requested URL not found'
			})