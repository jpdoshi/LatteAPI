from latteapi.utils.responses import TextResponse

def index(request):
	msg = "Hello, World!"
	response = TextResponse(msg)

	return response

# -----------------------------------------------

# from latteapi.utils.responses import TextResponse
# from models.car import Car
# from db import orm

# def index(request):
# 	try:
# 		first_car = orm.select(Car).get(3)
# 		orm.delete(first_car)
		
# 		msg = "Record deleted"
# 		response = TextResponse(msg)

# 		return response

# 	except Exception as e:
# 		response = TextResponse(str(e), status=500)
# 		return response