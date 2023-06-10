from .utils.requests import Request
from .utils.responses import TextResponse

class Latte():
	def __init__(self):
		self.routes = {}
		self.middlewares = []

	async def __call__(self, scope, receive, send):
		if scope['type'] == 'lifespan':
			await self.handle_ls(scope, receive, send)

		else:
			await self.handle_http(scope, receive, send)

	async def handle_ls(self, scope, receive, send):
			await send({'type': 'lifespan.startup.complete'})
			await receive()
			await send({'type': 'lifespan.shutdown.complete'})

	async def handle_http(self, scope, receive, send):
		assert scope['type'] == 'http'

		path = scope['path']
		parameter = None
		flag = 0

		_receive = await receive()
		request = Request(scope, _receive)

		for r in self.routes:
			url = r[0]
			handler = r[1]

			if url.find(":") != -1:
				pos = url.find(":")

				if path[pos:] != "":
					parameter = path[pos:]
					path = path[:pos]
					url = url[:pos]

			if path[-1] != "/":
				path = path + "/"

			if path == url:
				if parameter is not None:
					if parameter[-1] == "/":
						parameter = parameter[:-1]
					response = handler(request, parameter)
				else:
					response = handler(request)

				header  = response.header()
				body    = response.body()

				await send(header)
				await send(body)

				flag = 1
				break

		if flag == 0:
			response = TextResponse("Internal Server Error", status=500)

			header = response.header()
			body = response.body()

			await send(header)
			await send(body)
