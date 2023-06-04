# controller defines set of code to be executed for particular request
# it is possible to access request data and use, if needed
# response must be returned in order to complete task

# import models, middleware, response and utilities:
from latteapi.utils.responses import JSONResponse
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
