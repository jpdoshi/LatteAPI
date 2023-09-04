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
