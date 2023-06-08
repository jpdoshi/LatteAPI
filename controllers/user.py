from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.middleware import lattecache

@lattecache
def user(request):
	msg = request.params['id']
	return TextResponse("User ID: " + msg)
