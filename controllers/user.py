from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.middleware import lattecache

from latteapi.utils.conversion import jsonify
from models.user import User

@lattecache
def user(request, name):
	if request.method == "GET":
		user = User().get_user_by_name(name)

		if user is not None:
			response = JSONResponse(user)
		else:
			response = TextResponse("No user found", status=404)

		return response

	if request.method == "POST":
		user = User().create_user_by_name(name)

		if user is not None:
			response = TextResponse(user + " added")
		else:
			response = TextResponse("Could not create user", status=500)

		return response
