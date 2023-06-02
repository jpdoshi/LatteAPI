from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.utils.caching import cached

@cached
def index(request):
	msg = "Hello, World!"
	return TextResponse(msg)