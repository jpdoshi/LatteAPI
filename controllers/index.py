from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.middleware import lattecache

@lattecache
def index(request):
	msg = "Hello, World!"
	return TextResponse(msg)