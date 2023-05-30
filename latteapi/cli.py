import os

def generate_model(model):
	pass

def generate_controller(controller):
	try:
		_dir = 'controllers/'
		_name = str(controller + '.py')
		_file = _dir + _name

		if not os.path.exists(_file):
			with open(_file, 'w') as _f:
				_f.write(
f'''from latteapi.utils.responses import TextResponse, JSONResponse

def controller(request):
	msg = "{controller} works!"
	return TextResponse(msg)
''')
				print("Controller generated!")
		else:
			print("Controller already exists...")

	except Exception as e:
		print("Could not generate controller\n" + e)