# from latteapi.utils.responses import TextResponse

# def index(request):
# 	msg = "Hello, World!"
# 	response = TextResponse(msg)

# 	return response

# -----------------------------------------------

from latteapi.utils.responses import TextResponse
from models.car import Car
from db import orm

def index(request):
	try:
		car = Car(request.body)
		orm.save(car)
		
		msg = "Car Added!"
		response = TextResponse(msg)

		return response

	except Exception as e:
		response = TextResponse(e, status=500)
		return response