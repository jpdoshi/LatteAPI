class Latte():
	def __init__(self):
		self.routes = {}

	async def __call__(self, scope, receive, send):
		assert scope['type'] == 'http'

		path = scope['path']
		flag = 0

		for r in self.routes:
			if path == r:
				await send(self.routes[r].header())
				await send(self.routes[r].body())
				
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