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
		param = None
		flag = 0

		_receive = await receive()
		request = Request(scope, _receive)

		for r in self.routes:
			url = r[0]
			handler = r[1]

			if url.find(":") != -1:
				pos = url.find(":")

				if path[pos:] != "":
					param = path[pos:]
					path = path[:pos]
					url = url[:pos]

			if path[-1] != "/":
				path = path + "/"

			if path == url:
				if param is not None:
					if param[-1] == "/":
						param = param[:-1]
					_handler = handler(request, param)
				else:
					_handler = handler(request)

				_header  = _handler.header()
				_body    = _handler.body()

				await send(_header)
				await send(_body)

				flag = 1
				break

		if flag == 0:
			not_found = TextResponse("Internal Server Error", status=500)

			await send(not_found.header())
			await send(not_found.body())
