from latteapi.Latte import Latte
import routes

app = Latte(debug=True)
app.routes = routes.urls
