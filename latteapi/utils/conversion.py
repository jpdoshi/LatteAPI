import json

def jsonify(data, loads=False):
	if not loads:
		return json.dumps(data)
	else:
		return json.dumps(json.loads(data))
