from latteapi.http import TextResponse


def index(request):
	msg = "Something went wrong"

	if request.method == 'GET':
		msg = "Show Data"

	if request.method == 'POST':
		msg = "Insert Data"

	if request.method == 'PUT':
		msg = "Update Data"

	if request.method == 'DELETE':
		msg = "Remove Data"

	response = TextResponse(msg)
	return response
