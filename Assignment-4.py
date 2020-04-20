class ComplexNumber:
	def __init__(self, real=0, imag=0):
		self.real_part = real
		self.imaginary_part = imag
		if type(real)==str and type(imag)==str:
			raise ValueError('Invalid value for real and imaginary part')
		elif type(real)==str:
			raise ValueError('Invalid value for real part')
		elif type(imag)==str:
			raise ValueError('Invalid value for imaginary part')
		
	
	def __str__(self):
		return f"{self.real_part}{self.imaginary_part:+}i"
	
	def conjugate(self):
		return ComplexNumber(self.real_part,-self.imaginary_part)
	
	def __add__(self,other):
		self.real_part = self.real_part + other.real_part
		self.imaginary_part = self.imaginary_part + other.imaginary_part
		return ComplexNumber(self.real_part,self.imaginary_part)
	
	def __sub__(self,other):
		self.real_part = self.real_part - other.real_part
		self.imaginary_part = self.imaginary_part - other.imaginary_part
		return ComplexNumber(self.real_part,self.imaginary_part)
	
	def __mul__(self,other):
		real_part = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
		imaginary_part = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
		return ComplexNumber(real_part,imaginary_part)
	
	def __truediv__(self,other):
		conj = other.conjugate()
		den = other*conj
		den = den.real_part
		result = self*conj
		return ComplexNumber(result.real_part/den,result.imaginary_part/den)
		
	def __eq__(self,other):
		return bool(self.real_part == other.real_part and self.imaginary_part == other.imaginary_part)
	
	def __abs__(self):
		return round((self.real_part**2+self.imaginary_part**2)**0.5,3)
