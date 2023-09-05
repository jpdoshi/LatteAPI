import mimetypes


class Request():

	def __init__(self, scope, receive):

		self.body = receive['body'].decode('utf')

		self.method = scope['method']

		self.path = scope['path']

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


	def set_cookie(self, key, value, expires="", max_age="", path='/', secure=""):
		cookie = f"{key}={value}; expires={expires}; Max-Age={max_age}; Path={path}; {secure}"
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

	def __init__(self, data, mime, status: int=200):
		super().__init__(data, mime, status)


class RedirectResponse(Response):

	def __init__(self, url, data="", mime="", status: int=302):
		super().__init__(bytes(data, 'utf-8'), mime, status)
		super().set_headers([
			(b'Location', bytes(url, 'utf-8')),
		])
