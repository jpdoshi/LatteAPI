from latteapi.http import TextResponse


def index(request):
	msg = "Hello, World!"
	response = TextResponse(msg)

	return response
