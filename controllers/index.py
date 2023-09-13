from latteapi.http import TextResponse

def index(request):
	msg = "Hello, World!"

	response = TextResponse(msg)
	return response

# -----------------------------------------------

# from latteapi.websocket import WebSocket

# websocket = WebSocket()

# def index(websocket=websocket):
# 	websocket.accept()
# 	websocket.close()
