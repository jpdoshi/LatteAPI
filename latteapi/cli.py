import os

def setargs(arglist:list):
	try:
		_arg = arglist[0]

		if _arg == "controller":
			_name = arglist[1]
			gen_controller(_name)

		elif _arg == "model":
			_name = arglist[1]
			gen_model(_name)

		else:
			instruction()

	except:
		instruction()

def instruction():
	print("USAGE INSTRUCTION:")
	print("controller <name> : Generates controller")
	print("model      <name> : Generates model")

def gen_controller(controller):
	try:
		_dir = 'controllers/'
		_name = str(controller + '.py')
		_file = _dir + _name

		if not os.path.exists(_file):
			with open(_file, 'w') as _f:
				_f.write(
f'''from latteapi.utils.responses import TextResponse, JSONResponse

def {controller}(request):
	msg = "{controller} works!"
	response = TextResponse(msg)

	return response
''')
			print("INFO: Controller generated")
			print("MESSAGE: Remember to add route for controller")

		else:
			print("ERROR: Controller already exists")

	except Exception as e:
		print("EXCEPTION:\n", e)

def gen_model(model):
	try:
		_dir = 'models/'
		_name = str(model + '.py')
		_file = _dir + _name

		if not os.path.exists(_file):
			with open(_file, 'w') as _f:
				_f.write(
f'''from sqlalchemy import Column, Integer, String
from db import Base

class {model.capitalize()}(Base):
	__tablename__ = "{model}"

	id = Column(Integer, primary_key=True)
	# add fields

	def __init__(self):
		pass

	# add methods to return data

''')
			print("INFO: Model generated")

		else:
			print("ERROR: Model already exists")

	except Exception as e:
		print("EXCEPTION:\n", e)
