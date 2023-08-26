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

		self.set_body(bytes(self.data, 'utf-8'))

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
		super().__init__(data, "application/json", status)

class TextResponse(Response):
	def __init__(self, data: str, status: int=200):
		super().__init__(data, "text/plain", status)

class HTMLResponse(Response):
	def __init__(self, data: str, status: int=200):
		super().__init__(data, "text/html", status)
