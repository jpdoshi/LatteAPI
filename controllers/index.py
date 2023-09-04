from latteapi.http import TextResponse

def index(request):
	try:
		msg = "Hello, World!"
		response = TextResponse(msg)

		return response

	except Exception as e:
		response = TextResponse(str(e), status=500)
		return response

# -----------------------------------------------

# from latteapi.http import FileResponse, TextResponse
# from latteapi.utils import File
# import requests

# def index(request):
# 	try:
# 		f = File("/home/jainam/Documents/Internship Certificate.pdf")
# 		response = FileResponse(f, mime="application/pdf")

# 		return response

# 	except Exception as e:
# 		response = TextResponse(str(e), status=500)
# 		return response

# -----------------------------------------------

# from latteapi.http import TextResponse
# from models.car import Car
# from db import orm

# def index(request):
# 	try:
# 		car = Car("Lexus LFA")
# 		orm.save(car)
		
# 		msg = "Record created!"
# 		response = TextResponse(msg)

# 		return response

# 	except Exception as e:
# 		response = TextResponse(str(e), status=500)
# 		return response
