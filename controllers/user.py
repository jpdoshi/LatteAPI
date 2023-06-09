from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.middleware import lattecache

@lattecache
def user(request, id):
	msg = "User ID: " + id
	response = TextResponse(msg)

	return response
