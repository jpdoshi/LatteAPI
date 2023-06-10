from latteapi.utils.responses import TextResponse
from latteapi.middleware import lattecache

@lattecache
def index(request):
	msg = "Hello, World!"
	response = TextResponse(msg)

	return response