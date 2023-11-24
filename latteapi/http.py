class Request():

	def __init__(self, scope, receive):

		self.body = receive['body'].decode('utf')

		self.method = scope['method']

		self.path = scope['path']

		self.cookies = {}

		for h in scope['headers']:

			if h[0] == "cookie".encode('utf-8'):

				cookies_str = h[1].decode()
				cookies = cookies_str.split("; ")

				for c in cookies:

					cookie = c.split("=")
					self.cookies[cookie[0]] = cookie[1]

		self.meta = scope


class Response():

	def __init__(self, data, mime, status):

		self.data = data

		self.mime = mime

		self.status = status

		self.headers = None

		self.body = None


		self.set_headers([
			(b'Content-Type', bytes(self.mime, 'utf-8')),
		])

		self.set_body(self.data)

	def set_headers(self, headers):
		self.headers = headers


	def set_body(self, body):
		self.body = body


	def get_header(self) -> dict:
		return {
			'type': 'http.response.start',
			'status': self.status,
			'headers': self.headers,
		}


	def get_body(self) -> dict:
		return {
			'type': 'http.response.body',
			'body': self.body,
		}

	def addHeader(self, _h:tuple):
		self.headers.append(_h)


	def set_cookie(self, key, value, expires="", max_age=604800, path='/', secure=False):
		cookie = f"{key}={value}; expires={expires}; Max-Age={max_age}; Path={path};"

		if secure == True:
			cookie += "Secure"

		cookie_header = (b'Set-Cookie', bytes(cookie, 'utf-8'))
		self.addHeader(cookie_header)


class JSONResponse(Response):

	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "application/json", status)


class TextResponse(Response):

	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "text/plain", status)


class HTMLResponse(Response):

	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "text/html", status)


class XMLResponse(Response):

	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "application/xml", status)


class FileResponse(Response):

	def __init__(self, file, mime, status: int=200):
		super().__init__(file, mime, status)


class StreamingResponse():

	def __init__(self, stream, mime, status: int=200):

		self.stream = stream

		self.mime = mime

		self.status = status

		self.headers = [
			(b'Content-Type', bytes(self.mime, 'utf-8')),
		]


	def get_header(self) -> dict:

		return {
			'type': 'http.response.start',
			'status': self.status,
			'headers': self.headers,
		}


	def addHeader(self, _h:tuple):
		self.headers.append(_h)


	def set_cookie(self, key, value, expires="", max_age=604800, path='/', secure=False):
		cookie = f"{key}={value}; expires={expires}; Max-Age={max_age}; Path={path};"

		if secure == True:
			cookie += "Secure"

		cookie_header = (b'Set-Cookie', bytes(cookie, 'utf-8'))
		self.addHeader(cookie_header)


class RedirectResponse(Response):

	def __init__(self, url, data="", mime="", status: int=302):

		super().__init__(bytes(data, 'utf-8'), mime, status)

		super().set_headers([
			(b'Location', bytes(url, 'utf-8')),
		])
