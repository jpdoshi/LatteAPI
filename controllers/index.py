from latteapi.utils.responses import TextResponse

def index(request):
	msg = "Hello, World!"
	response = TextResponse(msg)

	return response