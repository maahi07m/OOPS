class User:
	def __init__(self,name,mobile_no,address=""):
		self.name = name
		self.mobile_no = mobile_no
		self.address = address
		
class BankAccount:
	def __init__(self,name,mobile_no):
		self.name = name
		self.mobile_no =mobile_no
		#self.acc_no = acc_no
		self.generate_account_no()
		self.balance = 0
	def generate_account_no(self):
		import uuid
		self.acc_no = str(uuid.uuid4())
	def deposit(self,amount):
		self.balance += amount
	def withdraw(self,amount):
		if amount>self.balance:
			print("Insufficent Funds!")
		else:
			self.balance -= amount
		
b = BankAccount("Mahi","1234656678")
print(b.name,b.mobile_no,b.acc_no,b.balance) #o/p: Mahi 1234656678 9876543211 0
b.generate_account_no()
print(b.acc_no) #eb7b866c-3cd0-48ec-a420-c1ee9b2dde54
b.deposit(1000)
print(b.balance)
b.withdraw(500)
print(b.balance)
b.withdraw(1000)
print(b.balance)
'''
output:
	Mahi 1234656678 03cd70c0-b14d-47f5-a52c-5779378c9ce1 0
eefcd02b-caef-4fe0-9964-58c4097751e1
1000
500
Insufficent Funds!
500
After removing acc_no and adding the 
creating the self.generate_account_no()
Mahi 1234656678 14bdcc58-19fb-434b-849f-2579ab7e2faa 0
5e94148e-6620-47f1-8107-09be17c3a4a6
'''
'''
class Car:
	def __init__(self , color,acceleration):
		self.color = color
		self.acceleration = acceleration
		self.speed = 0
	def accelerate(self):
		print("Speeding Up!!")
		self.speed += self.acceleration
	def apply_brakes(self):
		print("Applying Brakes")
		self.speed -= 10

car_1 = Car(color = 'Red',acceleration=70)
car_1.accelerate()
print(car_1.speed)
'''

'''
class Person:
	def __init__(self,full_name):
		self.name = full_name
	def say_hello(self):
		print("Hello i'm {}!".format(self.name))
'''		
'''
class Person:
	def __init__(self, name):
		print("Hello!  , I'm {}!".format(name))
		
	def say_hello(self):
		print('Hello')
		print(self)
		
	def greet(self , name='Person'):
		return "Hello {}".format(name)


class Mahesh:
	def __init__(self , name ,age , car):
		self.name = name
		self.age = age
		self.car = car
	def func(self):
		print('How are you '+self.name + ', got the '+self.car)
		
p1=Mahesh('mahi',36,'tesla')
'''
