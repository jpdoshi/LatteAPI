from latteapi.utils.responses import JSONResponse
from latteapi.middleware import lattecache

from latteapi.utils.conversion import jsonify
from models.user import User

@lattecache
def users(request):
	user_list = User().get_all_users()
	users = {
		"users": user_list
	}

	response = JSONResponse(jsonify(users))
	return response
