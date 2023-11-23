class WebSocket():

	def __init__(self, sender):
		self.sender = sender


	async def connect(self):
		await self.sender({
			'type': 'websocket.accept',
			'Upgrade': 'websocket',
			'Connection': 'Upgrade',
		})


	async def send(self, message):
		await self.sender({
			'type': 'websocket.send',
			'text': message,
		})


	async def receive(self, receiver):
		data = await receiver()
		return data['text']


	async def close(self):
		await self.sender({
			'type': 'websocket.close',
		})
