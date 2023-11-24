from latteapi.http import TextResponse

async def index(request):
	msg = "Hello, World!"
	response = TextResponse(msg)
	
	return response