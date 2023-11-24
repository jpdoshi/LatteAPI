# RESPONSES

## Plain Text

```python
from latteapi.http import TextResponse

async def index(request):
	msg = "Hello, World!"

	response = TextResponse(msg)
	return response
```

## JSON

```python
from latteapi.http import JSONResponse
from latteapi.utils import jsonify

async def index(request):
	msg = {"msg": "Hello, World!"}

	response = JSONResponse(jsonify(msg))    
	return response
```

## WebSocket

```python
from latteapi.websocket import WebSocket
import time

async def index(receiver, sender):
	ws = WebSocket(sender)

	await ws.connect()
	await ws.send("Hey There!")
	
	time.sleep(1.0)
	await ws.send("What's Your Name?")
	name = await ws.receive(receiver)
	
	time.sleep(1.0)
	await ws.send("Hello, " + name)
	await ws.close()
```