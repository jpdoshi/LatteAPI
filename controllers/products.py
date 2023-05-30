from latteapi.utils.responses import TextResponse, JSONResponse

def controller(request):
	msg = "products works!"
	return TextResponse(msg)
