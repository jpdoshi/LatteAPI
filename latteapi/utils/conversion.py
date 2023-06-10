import json

def jsonify(data):
	return json.dumps(data)

def stringify(data):
	return json.loads(data)
