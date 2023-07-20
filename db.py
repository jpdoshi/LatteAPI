from latteapi.db import ORM

orm = ORM(DB_URI="sqlite:///db.sqlite")
Base = orm.base