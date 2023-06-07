class Response():
	def __init__(self):
		self.data = ""
		self.mime = ""
		self.status = 200

	def header(self):
		headers = [
			(b'Content-Type', bytes(self.mime, 'utf-8')),
			(b'Content-Length', bytes(str(len(self.data)), 'utf-8')),
		]

		return {
			'type': 'http.response.start',
			'status': self.status,
			'headers': headers,
		}

	def body(self):
		body = bytes(self.data, 'utf-8')

		return {
			'type': 'http.response.body',
			'body': body,
		}

class JSONResponse(Response):
	def __init__(self, data: str, status=200):
		self.data = data
		self.mime = 'application/json'
		self.status = status

class TextResponse(Response):
	def __init__(self, data: str, status=200):
		self.data = data
		self.mime = 'text/plain'
		self.status = status

class NotFound(Response):
	def __init__(self, data: str):
		self.data = data
		self.mime = 'text/plain'
		self.status = 404

class BadRequest(Response):
	def __init__(self, data: str):
		self.data = data
		self.mime = 'text/plain'
		self.status = 400