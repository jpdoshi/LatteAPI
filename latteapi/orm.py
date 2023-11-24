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


	def save(self, model):
		self.migrate()
		self.session.add(model)
		self.session.commit()


	def delete(self, model):
		self.session.delete(model)
		self.session.commit()
