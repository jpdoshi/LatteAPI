from latteapi.Latte import Latte
from settings import middlewares

import routes

app = Latte()
app.middlewares = middlewares
app.routes = routes.urls