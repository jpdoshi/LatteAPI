from .http import Request
from .http import TextResponse, StreamingResponse

from .debug import ShowException
import traceback


class LatteAPI():

	def __init__(self, debug=False):

		self.routes = {}

		self.middlewares = []

		self.trusted_hosts = [
			'127.0.0.1',
		]

		self.debug = debug


	def add_middleware(self, middleware):
		self.middlewares.append(middleware)


	async def __call__(self, scope, receive, send):

		host = scope['client'][0]

		for h in self.trusted_hosts:

			if h == host or h == '*':

				if scope['type'] == 'lifespan':
					await self.handle_ls(scope, receive, send)

				elif scope['type'] == 'websocket':
					await self.handle_websocket(scope, receive, send)

				else:
					await self.handle_http(scope, receive, send)


	async def handle_ls(self, scope, receive, send):

		await send({
			'type': 'lifespan.startup.complete'
		})

		await receive()

		await send({
			'type': 'lifespan.shutdown.complete'
		})


	async def handle_websocket(self, scope, receive, send):

		path = scope['path']

		for r in self.routes:
			url = r[0]
			handler = r[1]


			if path[-1] != "/":
				path = path + "/"


			if path == url:

				rec = await receive()
						
				if rec['type'] == 'websocket.accept':
					pass
						
				else:
					handler(receive, send)


	async def handle_http(self, scope, receive, send):

		assert scope['type'] == 'http'
		path = scope['path']

		parameter = None

		try:

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

						response = await handler(request, parameter)

					else:
						response = await handler(request)

					if self.middlewares is not None:

						for middleware in self.middlewares:
							m = middleware(response)
							response = m


					if isinstance(response, StreamingResponse):

						header:dict = response.get_header()
						await send(header)

						for chunk in response.stream:
							await send({
								'type': 'http.response.body',
								'body': chunk,
								'more_body': True,
							})

						await send({
							'type': 'http.response.body',
							'body': "",
							'more_body': False,
						})

					else:

						header:dict = response.get_header()
						body:dict = response.get_body()

						await send(header)
						await send(body)

						break


		except Exception as e:

			if self.debug == False:
				response = TextResponse(e, status=500)

			else:
				exc = ShowException(traceback.format_tb(e.__traceback__), traceback.format_stack())
				response = exc()

			header:dict = response.get_header()
			body:dict = response.get_body()

			await send(header)
			await send(body)
