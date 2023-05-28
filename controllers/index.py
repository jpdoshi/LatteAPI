from utils.responses import TextResponse

def controller(request):
	msg = "Hello, World!"
	return TextResponse(msg)