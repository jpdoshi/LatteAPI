import json


def jsonify(data):
	return json.dumps(data)


def stringify(data):
	return json.loads(data)


def Form(request) -> dict:
	body = request.body
	return json.loads(body)


def File(url: str) -> bin:
	f = open(url, "rb")
	data = f.read()
	return data


def Stream(data):
	for chunk in data:
		yield chunk.encode('utf-8')


def FileStream(url: str, chunk_size: int=64):
	with open(url, "rb") as f:
			while True:
				chunk = f.read(chunk_size)
				if not chunk:
					break
				yield chunk
