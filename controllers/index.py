# controller defines set of code to be executed for particular request
# it is possible to access request data and use, if needed
# response must be returned in order to complete task

# import models, middleware, response and utilities:
from latteapi.utils.responses import TextResponse
from latteapi.middleware import lattecache

@lattecache
def index(request):
	msg = "Hello, World!"
	return TextResponse(str(msg))