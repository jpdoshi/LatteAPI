from latteapi.utils.responses import TextResponse, JSONResponse
from latteapi.utils.conversion import jsonify
from models import user

import json

def controller(request):
	user_list = user.model()
	user_list.pop(-1)
	
	_list = {
		"users": user_list
	}
	return JSONResponse(jsonify(_list))