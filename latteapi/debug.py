# IMPORTS:
# ---------------------------------------------------------

from .http import HTMLResponse


# ShowException Object:
# ---------------------------------------------------------

class ShowException():
	# initialize exception attributes
	def __init__(self, stack: list, extra: list):
		self.stack = stack
		self.extra = extra

	# handle call function
	def __call__(self):
		# exception page HTML code
		html = """
		<head>
		<style>
			* {
				margin: 0;
				padding: 0;
				font-family: arial, helvetica;
				box-sizing: border-box;
			}

			body {
				color: #8d6e63;
				background-color: #efebe9;
			}

			.container {
				width: 1200px;
				max-width: 100%;
				margin: 32px auto;
				padding-inline: 1.5rem;
			}

			h1 {
				font-weight: normal;
			}

			.highlight {
				font-weight: bold;
			}

			.spacer {
				margin: 2rem 0;
			}

			.frame-stack .frame:nth-child(1) {
				border-top-left-radius: 1rem;
				border-top-right-radius: 1rem;
			}

			.frame-stack .frame:nth-last-child(1) {
				border-bottom-left-radius: 1rem;
				border-bottom-right-radius: 1rem;
			}

			.frame {
				margin: 4px 0;
				padding: 12px;
				font-family: consolas, monospace;
				font-size: 15px;
				background-color: #fafafa;
			}
		</style>
		</head>
		<body>
			<div class="container">
				<div class="spacer">
					<h1 style="margin-bottom: 8px">Exception Occured</h1>
					<hr color="#d7ccc8" style="margin-bottom: 1rem">
					<p>Something went wrong in the application, To prevent
					this page from showing, set <span class="highlight">Debug=False</span>
					in <span class="highlight">app.py</span> file.</p>
				</div><div class="frame-stack">
		"""

		# show necessary exception
		self.stack.pop(0)
		self.extra.pop(0)

		# show error stack
		for line in self.stack:
			html += "<div class=\"frame\">" + line + "</div>"

		html += """
		</div>
		<div class=\"spacer\">
			<h1 style="margin-bottom: 8px">Extra Information</h1>
			<hr color="#d7ccc8" style="margin-bottom: 1rem">
			<p>Below shown is complete error stack, which can be used to check if
			there's a problem in the application or any external factors.</p>
		</div><div class="frame-stack">"""

		# show full error stack
		for line in self.extra:
			html += "<div class=\"frame\">" + line + "</div>"

		html += "</div></div></body>"

		# show exception page in response
		return HTMLResponse(html, status=500)
