class Response():
	def __init__(self):
		self.data = ""
		self.mime = ""
		self.status = 200

	def header(self):
		return {
			'type': 'http.response.start',
			'status': self.status,
			'headers': [
				(b'content-type', bytes(self.mime, 'utf-8')),
			],
		}

	def body(self):
		return {
			'type': 'http.response.body',
			'body': bytes(self.data, 'utf-8'),
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