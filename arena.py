'''
An arena is a place where pokemons get together. an arena contains pokemons
you can add a pokemon to an arena: this uses add on the arena instance. Only pokemons or creatures inheriting from pokemons can be added to an arena. a pokemon can also join an arena with the join method: pokemon.join(arena). Implement this method on the Pokemon class. Do not make any type checks - you only need a single line of code in that method! the active method returns a list of all active pokemons (i.e. whose health is > 0) in the arena the "length" of the arena is the number of active pokemons in it the method get_pokemons returns a list of all pokemons, sorted by name it is possible to load pokemons from a file into an arena with the load_from_file method load_from_file takes one argument: the name of the file to read from the file is in CSV format and has three columns: name, health and level of the pokemons
'''
from pokemon import Pokemon
#import csv
import csv

class Arena:
	def __init__(self):
		self.all_pokemons = []
		self.active_pokemons = []
		pass

	def add(self, pokemon):
		#Add a pokemon to the arena
		self.all_pokemons.append(pokemon)
		#If the pokemon's health is above 0, add it to the active pokemons list
		if pokemon.health > 0:
			self.active_pokemons.append(pokemon)

	def __len__(self):
		#the length of the arena is the number of active pokemons

		# use remove_fained to remove any pokemon with 0 health
		self.remove_fained()

		return len(self.active_pokemons)



	def get_pokemons(self):
		#the method get_pokemons returns a list of all pokemons, sorted by name
		return sorted(self.all_pokemons, key=lambda x: x.name)

	def active(self):
		#the active method returns a list of all active pokemons (i.e. whose health is > 0)

		#use remove_fained to remove any pokemon with 0 health
		self.remove_fained()

		return sorted(self.active_pokemons, key=lambda x: x.name)

	#Helper Method to go through active pokemons and remove any with 0 health
	def remove_fained(self):
		for pokemon in self.active_pokemons:
			if pokemon.health <= 0:
				self.active_pokemons.remove(pokemon)


	def load_from_file(self, filename):
		#the method load_from_file takes one argument: the name of the file to read from the file is in CSV format and has three columns: name, health and level of the pokemons

		#Note to self: File is a csv. Need some csv libraries
		#Open and read csv file
		with open(filename) as file:
			reader = csv.reader(file)
			#Note: File has header row. Skip it
			next(reader) #skip header row
			for row in reader:
				name = row[0]
				health = int(row[1])
				level = int(row[2])
				#Note: Name and Health can be added directly. But Level can't. What if I use a while loop to run the add_level method over and over until we get the right level? But.....how do I do that?
				#Here's my idea
				#Step 1: Just add the Pokemon with the name and health first
				pokemon = Pokemon(name, health)
				self.add(pokemon)

				#Step 2: Then add the level
				pokemon.level = level