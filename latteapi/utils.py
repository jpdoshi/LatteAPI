# IMPORTS:
# ---------------------------------------------------------

import json


# UTILITY METHODS:
# ---------------------------------------------------------

# converts dictionary to json string
def jsonify(data):
	return json.dumps(data)

# converts json string to dictionary
def stringify(data):
	return json.loads(data)

# returns dictionary from json data of request
def Form(request) -> dict:
	body = request.body
	return json.loads(body)

def File(url: str) -> bin:
	f = open(url, "rb")
	data = f.read()
	return data
