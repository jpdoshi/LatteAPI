from latteapi.utils.responses import TextResponse
from latteapi.middleware import cache

@cache()
def index(request):
	msg = "Hello, World!"
	response = TextResponse(msg)

	return response