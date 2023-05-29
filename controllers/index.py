from latteapi.utils.responses import TextResponse, JSONResponse

def controller(request):
	msg = "Hello, World!"
	return TextResponse(msg)