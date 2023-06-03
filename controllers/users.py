from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.middleware import lattecache

from latteapi.utils.conversion import jsonify
from models import user

@lattecache
def users(request):
	user_list = user.model()
	user_list.pop(-1)
	
	_list = {
		"users": user_list
	}
	return JSONResponse(jsonify(_list))
