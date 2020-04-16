class Car:
	def __init__(self,color, max_speed, acceleration, tyre_friction):
		self.color = color
		self.max_speed = max_speed
		self.acceleration = acceleration
		self.tyre_friction = tyre_friction
		self.is_engine_started = False
		self._current_speed = 0 
		self.check_valid(max_speed,'max_speed')
		self.check_valid(acceleration,'acceleration')
		self.check_valid(tyre_friction,'tyre_friction')
		
	@staticmethod
	def check_valid(valid,attribute):
		try:
			if valid > 0:
				pass
			else:
				raise ValueError
		except ValueError:
			print(f'ValueError: Invalid value for {attribute}')
		
		
	@property
	def current_speed(self):
		return self._current_speed
	
	def start_engine(self):
		self.is_engine_started = True
	
	def stop_engine(self):
		self.is_engine_started = False
	
	def accelerate(self):
		if self.is_engine_started == True:
			if self._current_speed+self.acceleration >= self.max_speed:
				return self.max_speed
			else:
				self._current_speed += self.acceleration
		else:
			print('Start the engine to accelerate')
	
	def apply_brakes(self):
		self._current_speed -= self.tyre_friction
	
	def sound_horn(self):
		if self.is_engine_started == True:
			print('Beep Beep')
		else:
			print('Start the engine to sound_horn')
			
