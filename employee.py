class Employee:

	raise_amt = 1.05
	
	def __init__(self,first,last,pay):
		self.fname = first
		self.lname = last
		self.pay = pay
	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amt)
class Developer(Employee):
	raise_amt = 1.06
	def __init__(self,first, last, pay, prog_name):
		super().__init__(first,last,pay)
		self.prog_lang = prog_name
        
class Manager(Employee):
	def __init__(self,first, last, pay, employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)
	def remove_emp(self,emp):
		if emp not in self.employees:
			self.employees.remove(emp)
	def print_emps(self):
		for emp in self.employees:
			print('-->',emp.fullname())

            
        
            
 
        
dev_1 = Developer('mahi','mahesh',50000,'python')
dev_2 =	Developer('rakhi','rakesh',49999,'java')
mgr_1 = Manager('sue','smith',90000,[dev_1])
mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())



#print(dev_1.prog_lang)
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
