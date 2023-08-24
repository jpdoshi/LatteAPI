from .utils.responses import HTMLResponse

class ShowException():
	def __init__(self, exc: str, stack: str):
		self.exc = exc
		self.stack = stack

	def __call__(self):
		page = """
		<head>
		<style>
			* {
				margin: 0;
				padding: 0;
				font-family: arial;
				box-sizing: border-box;
			}

			body {
				width: 85%;
				color: #8d6e63;
				margin: 24px auto;
				background-color: #efebe9;
			}

			.heading, .exception {
				margin-inline: 1rem;
				font-weight: normal;
			}

			.exception {
				margin-bottom: 2rem;
			}

			.trace {
				margin: 1rem;
				padding: 10px;
				border-radius: 6px;
				font-family: monospace, consolas;
				font-size: 15px;
				background-color: #fafafa;
			}
		</style>
		</head>
		<body>
			<h1 class="heading">Exception Occured</h1><br>
			<p class="exception"> """ + self.exc +""" </p>
		</body>
		"""
		for line in self.stack:
			page += "<div class=\"trace\">" + line + "</div>"
		return HTMLResponse(page, status=500)