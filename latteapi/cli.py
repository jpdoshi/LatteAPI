import os

def setargs(arglist:list):
	try:
		_arg = arglist[0]

		if _arg == "gc":
			_name = arglist[1]
			gen_controller(_name)

		elif _arg == "gm":
			_name = arglist[1]
			gen_model(_name)

		elif _arg == "migrate":
			migrate()

		else:
			instruction()

	except:
		instruction()

def instruction():
	print("USAGE INSTRUCTION:")
	print("gc <name> : Generates controller")
	print("gm <name> : Generates Model")
	print("migrate   : Database Migration")

def migrate():
	try:
		print("Migrating...")

	except Exception as e:
		print("EXCEPTION:\n", e)

def gen_model(model):
	pass

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