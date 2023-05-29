class Response():
	def __init__(self):
		self.data = ""
		self.mime = ""

	def header(self):
		return {
			'type': 'http.response.start',
			'status': 200,
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
	def __init__(self, data: str):
		self.data = data
		self.mime = 'application/json'

class TextResponse(Response):
	def __init__(self, data: str):
		self.data = data
		self.mime = 'text/plain'