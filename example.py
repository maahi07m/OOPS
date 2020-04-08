class Employee:

	def __init__(self,first,last):
		self.fname = first
		self.lname = last
	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)
    
emp_1 = Employee('mahi','mahesh')
emp_2 = Employee('rakhi','rakesh')

#print('{} {}'.format(emp_1.fname,emp_1.lname))
#print('{} {}'.format(emp_2.fname,emp_2.lname))
print(emp_2.fullname())
print(Employee.fullname(emp_1))

