class Car:
	def __init__(self,color='Black', max_speed=0, acceleration=0, tyre_friction=0):
		self._color = color
		self._max_speed = max_speed
		self._acceleration = acceleration
		self._tyre_friction = tyre_friction
		self._is_engine_started = False
		self._current_speed = 0
		
		self.check_valid(max_speed,'max_speed')
		self.check_valid(acceleration,'acceleration')
		self.check_valid(tyre_friction,'tyre_friction')
		
	@staticmethod
	def check_valid(valid,attribute):
		try:
			if valid >= 0:
				pass
			else:
				raise ValueError
		except ValueError:
			raise ValueError('Invalid value for {}'.format(attribute))
	
	@property
	def color(self):
		return self._color
	
	@property
	def max_speed(self):
		return self._max_speed
	
	@property
	def acceleration(self):
		return self._acceleration
	
	@property
	def tyre_friction(self):
		return self._tyre_friction
	
	@property
	def is_engine_started(self):
		return self._is_engine_started
	
	@property
	def current_speed(self):
		return self._current_speed
	
	def start_engine(self):
		self._is_engine_started = True
	
	def stop_engine(self):
		self._is_engine_started = False
	
	def accelerate(self):
		if self.is_engine_started == True:
			if self._current_speed+self.acceleration >= self.max_speed:
				self._current_speed = self.max_speed
			else:
				self._current_speed += self.acceleration
		else:
			print('Start the engine to accelerate')
	
	def apply_brakes(self):
		if self._current_speed-self.tyre_friction >= 0:
			self._current_speed -= self.tyre_friction
		else:
			self._current_speed = 0
	
	def sound_horn(self):
		if self._is_engine_started == True:
			print('Beep Beep')
		else:
			print('Start the engine to sound_horn')
			
