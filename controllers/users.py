from utils.responses import JSONResponse
from models import user

def controller(request):
	user_list = user.model()
	user_list.pop(-1)
	return JSONResponse({"users": user_list})