from latteapi.http import TextResponse, JSONResponse

async def users(request, id):
	msg = "USER ID: %s" % id
	
	response = TextResponse(msg)
	return response
