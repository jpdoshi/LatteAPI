# IMPORTS:
# ---------------------------------------------------------

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# ORM Object
# ---------------------------------------------------------

class ORM():
	# initialize ORM class
	def __init__(self, DB_URI:str):
		# initialize SQLAlchemy attributes
		self.base = declarative_base()
		self.engine = create_engine(DB_URI)

		Session = sessionmaker(bind=self.engine)
		self.session = Session()

	# ORM Methods:

	# initialize all tables
	def migrate(self):
		self.base.metadata.create_all(self.engine)

	# return query data
	def select(self, model):
		return self.session.query(model)

	# update all data in db
	def update(self):
		self.session.commit()

	# add data to db
	def save(self, data):
		self.migrate()
		self.session.add(data)
		self.session.commit()

	# remove data from db
	def delete(self, data):
		self.session.delete(data)
		self.session.commit()
