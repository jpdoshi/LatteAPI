import mimetypes

# REQUEST OBJECT:
# ---------------------------------------------------------

class Request():
	# get request parameters from request
	def __init__(self, scope, receive):
		# request body parameter
		self.body = receive['body'].decode('utf')

		# request method:get/post/delete/etc
		self.method = scope['method']

		# request url endpoint
		self.path = scope['path']

		# all request data
		self.meta = scope


# RESPONSE OBJECTS:
# ---------------------------------------------------------

# Response Parent Object
class Response():
	# initialize response object
	def __init__(self, data, mime, status):
		# initialize response attributes
		self.data = data
		self.mime = mime
		self.status = status

		self.headers = None
		self.body = None

		# set initial headers
		self.set_headers([
			(b'Content-Type', bytes(self.mime, 'utf-8')),
		])

		# set data in response body
		self.set_body(self.data)

	# Response Methods:

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

	# set cookie with the response
	def set_cookie(self, key, value, expires="", max_age="", path='/', secure=""):
		cookie = f"{key}={value}; expires={expires}; Max-Age={max_age}; Path={path}; {secure}"
		cookie_header = (b'Set-Cookie', bytes(cookie, 'utf-8'))

		self.addHeader(cookie_header)


# DERIVED RESPONSE CLASSES:
# ---------------------------------------------------------

# JSON Response Object
class JSONResponse(Response):
	# initialize JSON Response
	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "application/json", status)

# Text Response Object
class TextResponse(Response):
	# initialize Plain Text Response
	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "text/plain", status)

# HTML Response Object
class HTMLResponse(Response):
	# initialize HTML / Web Response
	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "text/html", status)

class XMLResponse(Response):
	# initialize XML Response
	def __init__(self, data: str, status: int=200):
		super().__init__(bytes(data, 'utf-8'), "application/xml", status)

class FileResponse(Response):
	# initialize File Response
	def __init__(self, data, mime, status: int=200):
		super().__init__(data, mime, status)

class RedirectResponse(Response):
	# initialize Redirect Response
	def __init__(self, url, data="", mime="", status: int=302):
		super().__init__(bytes(data, 'utf-8'), mime, status)
		super().set_headers([
			(b'Location', bytes(url, 'utf-8')),
		])