import json

def Form(request) -> dict:
	body = request.body
	return json.loads(body)
