from latteapi.http import TextResponse

def index(request):
	msg = "Hello, World!"

	response = TextResponse(msg)
	return response

# -----------------------------------------------

# from latteapi.websocket import WebSocket
# import time

# async def index(receiver, sender):
# 	ws = WebSocket(sender)

# 	await ws.connect()
# 	await ws.send("Hey There!")
	
# 	time.sleep(1.0)
# 	await ws.send("What's Your Name?")
# 	name = await ws.receive(receiver)
	
# 	time.sleep(1.0)
# 	await ws.send("Hello, " + name)
# 	await ws.close()
