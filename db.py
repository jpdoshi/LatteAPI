# import dependencies
from latteapi.orm import ORM


# initialize SQLAlchemy ORM
orm = ORM(DB_URI="sqlite:///db.sqlite")
Base = orm.base
