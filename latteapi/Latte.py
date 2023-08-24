from .utils.requests import Request
from .utils.responses import TextResponse

from .debug import ShowException

import traceback
import sys

class Latte():
	# initialize application
	def __init__(self, debug=True):
		self.routes = {}
		self.middlewares = []
		self.debug = debug

	def add_middleware(self, middleware):
		self.middlewares.append(middleware)

	# serve application
	async def __call__(self, scope, receive, send):
		# handle lifespan exception
		if scope['type'] == 'lifespan':
			await self.handle_ls(scope, receive, send)

		# handle http requests
		else:
			await self.handle_http(scope, receive, send)

	# lifespan handling
	async def handle_ls(self, scope, receive, send):
			await send({'type': 'lifespan.startup.complete'})
			await receive()
			await send({'type': 'lifespan.shutdown.complete'})

	# http request handling
	async def handle_http(self, scope, receive, send):
		# prerequisite
		assert scope['type'] == 'http'
		path = scope['path']

		# initialize attributes
		parameter = None
		# flag = 0

		try:
			# create request object
			_receive = await receive()
			request = Request(scope, _receive)

			# handle routes
			for r in self.routes:
				url = r[0]
				handler = r[1]

				# handle parameters
				if url.find(":") != -1:
					pos = url.find(":")

					if path[pos:] != "":
						parameter = path[pos:]
						path = path[:pos]
						url = url[:pos]

				# decorate url
				if path[-1] != "/":
					path = path + "/"

				# create response object
				if path == url:
					if parameter is not None:
						if parameter[-1] == "/":
							parameter = parameter[:-1]

						response = handler(request, parameter)

					else:
						response = handler(request)

					if self.middlewares is not None:
						for middleware in self.middlewares:
							m = middleware(response)
							response = m

					# fetch response data
					header:dict = response.get_header()
					body:dict = response.get_body()

					# serve response data
					await send(header)
					await send(body)

					# response over
					break

		# handle http exception
		except Exception as e:
			# create error response
			if self.debug == False:
				response = TextResponse("Internal Server Error", status=500)

			else:
				exc_type, exc_value, exc_tb = sys.exc_info()
				tb = traceback.TracebackException(exc_type, exc_value, exc_tb)

				exc = ShowException(''.join(tb.format_exception_only()), traceback.format_tb(e.__traceback__))
				response = exc()

			# fetch response data
			header:dict = response.get_header()
			body:dict = response.get_body()

			# serve response data
			await send(header)
			await send(body)
