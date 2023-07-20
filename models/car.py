from sqlalchemy import Column, Integer, String
from db import Base

class Car(Base):
	__tablename__ = "car"

	id = Column(Integer, primary_key=True)
	model = Column(String)

	def __init__(self, model):
		self.model = model

	# add methods to return data
