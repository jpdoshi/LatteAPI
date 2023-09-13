# import dependencies:
from latteapi import LatteAPI
import routes


# initialize app:
app = LatteAPI(debug=True)
app.routes = routes.urls
