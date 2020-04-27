class Pokemon:
	sound = ""
	is_type = ""
	def __init__(self, name="", level=1):
		self._name = name
		if name == "":
			raise ValueError("name cannot be empty")
		self._level = level
		self.is_attack = level
		self._master = ""
		if level<=0:
			raise ValueError("level should be > 0")
	
	@property
	def master(self):
		if self._master == "":
			print("No Master")
		else:
			return self._master

	@property
	def name(self):
		return self._name
	
	@property
	def level(self):
		return self._level
	
	@classmethod
	def make_sound(cls):
		print(cls.sound)

	def __str__(self):
		return f"{self._name} - Level {self._level}"
	
	@classmethod
	def run(cls):
		print(f"{cls.__name__} running...")
	
	@classmethod
	def swim(cls):
		print(f"{cls.__name__} swimming...")
	
	@classmethod
	def fly(cls):
		print(f"{cls.__name__} flying...")

class Pikachu(Pokemon):
	sound = "Pika Pika"
	def attack(self):
		print(f"Electric attack with {self.level*10} damage")
	
class Squirtle(Pokemon):
	sound = "Squirtle...Squirtle"
	def attack(self):
		print(f"Water attack with {self.level*9} damage")
	
class Pidgey(Pokemon):
	sound = "Pidgey...Pidgey"
	def attack(self):
		print(f"Air attack with {self.level*5} damage")
	
class Swanna(Pokemon):
	sound = "Swanna...Swanna"
	def attack(self):
		print(f"Water attack with {self.level*9} damage")
		print(f"Air attack with {self.level*5} damage")
	
class Zapdos(Pokemon):
	sound = "Zap...Zap"
	def attack(self):
		print(f"Electric attack with {self.level*10} damage")
		print(f"Air attack with {self.level*5} damage")
	
class Island:
	all_islands_list = []
	def __init__(self, name=None, max_no_of_pokemon=0, total_food_available_in_kgs=0):
		self._name = name
		self._max_no_of_pokemon = max_no_of_pokemon
		self._total_food_available_in_kgs = total_food_available_in_kgs
		self._pokemon_left_to_catch = 0
		Island.all_islands_list.append(self)

	@property
	def pokemon_left_to_catch(self):
		return self._pokemon_left_to_catch
	
	@property
	def name(self):
		return self._name
	
	@property
	def max_no_of_pokemon(self):
		return self._max_no_of_pokemon
	
	@property
	def total_food_available_in_kgs(self):
		return self._total_food_available_in_kgs
	
	def add_pokemon(self,pokemon):
		if self._pokemon_left_to_catch+1 <= self._max_no_of_pokemon:
			self._pokemon_left_to_catch+=1
		else:
			print("Island at its max pokemon capacity")
	
	def __str__(self):
		return ("{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))          
		
	@classmethod
	def get_all_islands(cls):
		return Island.all_islands_list
	
class Trainer:
	def __init__(self, name=None):
		self._name = name
		self._experience = 100
		self._max_food_in_bag = 10*self._experience
		self._food_in_bag = 0
		self._current_island = None
		self.pokemon_list = []
		
	@property
	def current_island(self):
		if self._current_island == None:
			print("You are not on any island")
		else:
			return self._current_island

	@property
	def name(self):
		return self._name
	
	@property
	def experience(self):
		return self._experience
	
	@property
	def max_food_in_bag(self):
		return self._max_food_in_bag
	
	@property
	def food_in_bag(self):
		return self._food_in_bag
		
	def move_to_island(self,island):
		self._current_island = island
		
	def catch(self,pokemon):
		if self._experience >= 100*pokemon.level:
			print(f"You caught {pokemon.name}")
			self.pokemon_list.append(pokemon)
			pokemon._master = self
			self._experience += 20*pokemon.level
		else:
			print(f"You need more experience to catch {pokemon.name}")
			
	def collect_food(self):
		if self._current_island == None:
			print("Move to an island to collect food")
			
		elif self._current_island.total_food_available_in_kgs < self._max_food_in_bag:
			self._food_in_bag = self._current_island._total_food_available_in_kgs
			self._current_island._total_food_available_in_kgs = 0

		elif self._food_in_bag != self._max_food_in_bag:
				self._food_in_bag = self._max_food_in_bag
				self._current_island._total_food_available_in_kgs -= self._max_food_in_bag

	def get_my_pokemon(self):
		return self.pokemon_list

	def __str__(self):
		return self._name
