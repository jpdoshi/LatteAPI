# import dependencies:
from latteapi.Latte import Latte
import routes


# initialize app:
app = Latte(debug=True)
app.routes = routes.urls
