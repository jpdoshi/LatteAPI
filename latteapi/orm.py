from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class ORM():

	def __init__(self, DB_URI:str):

		self.base = declarative_base()

		self.engine = create_engine(DB_URI)

		Session = sessionmaker(bind=self.engine)

		self.session = Session()


	def migrate(self):
		self.base.metadata.create_all(self.engine)


	def select(self, model):
		return self.session.query(model)


	def update(self):
		self.session.commit()


	def save(self, data):
		self.migrate()
		self.session.add(data)
		self.session.commit()


	def delete(self, data):
		self.session.delete(data)
		self.session.commit()
