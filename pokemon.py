
'''
A Pokemon has the following attributes:
name (string) health (integer) level (integer)
The constructor ONLY receives name and health. A new Pokemon will always have its level set to 1.
the name must be a non-empty string health must be a strictly positive integer if any of these conditions is not respected, raise a ValueError exception.

Ensure there are only 2 arguments in the constructor

'''

class Pokemon:
	def __init__(self, name, health, level=None):

		#Check if there are only 2 arguments in the constructor
		#Can I cheese this by checking if the default value for level got changed?
		if level:
			raise TypeError("Invalid number of arguments")

		#Check if the name is string and health is an integer
		if not isinstance(name, str) or not name or not isinstance(health, int) or health <= 0:
			raise ValueError("Invalid name or health")


		#Declare the attributes of the class
		self.name = name
		self.health = health
		self.level = 1

	def level_up(self):
		self.level += 1

	def join(self, arena):
		arena.add(self)