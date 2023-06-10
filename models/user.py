# temporary data store:
users = ["jon", "arya", "sansa", "robb", "bran"]

class User():
	def __init__(self):
		self.users = users

	def get_user_by_name(self, name):
		try:
			for user in self.users:
				if user == name:
					return user

		except:
			return None

	def create_user_by_name(self, name):
		try:
			self.users.append(name)
			return name
		except:
			return None

	def get_all_users(self):
		return self.users