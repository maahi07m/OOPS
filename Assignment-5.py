class Store:
	#store_item = []
	def __init__(self):
		self.store_item = []
		
	def __str__(self):
		if self.store_item == []:
			return 'No items'
		return '\n'.join(map(str,self.store_item))
	
	def add_item(self,item):
		self.store_item.append(item)
	
	def count(self):
		return len(self.store_item)
	
	def filter(self, q_object):
		store_obj = Store()
		if q_object.operation == "EQ":
			for i in self.store_item:
				if q_object.value == i.name:
					store_obj.add_item(i)
				elif q_object.value == i.category:
					store_obj.add_item(i)
				elif q_object.value == i.price:
					store_obj.add_item(i)
		
		elif q_object.operation == "GT":
			for i in self.store_item:
				if q_object.value < i.price:
					store_obj.add_item(i)
		
		elif q_object.operation == "GTE":
			for i in self.store_item:
				if q_object.value <= i.price:
					store_obj.add_item(i)
		
		elif q_object.operation == "LT":
			for i in self.store_item:
				if q_object.value > i.price:
					store_obj.add_item(i)
		
		elif q_object.operation == "LTE":
			for i in self.store_item:
				if q_object.value >= i.price:
					store_obj.add_item(i)
		
		elif q_object.operation == "STARTS_WITH":
			for i in self.store_item:
				if i.name.startswith(q_object.value) or i.category.startswith(q_object.value):
					store_obj.add_item(i)
		
		elif q_object.operation == "ENDS_WITH":
			for i in self.store_item:
				if i.name.endswith(q_object.value) or i.category.endswith(q_object.value):
					store_obj.add_item(i)
		
		elif q_object.operation == "IN":
			for i in self.store_item:
				if i.name in q_object.value or i.category in q_object.value or i.price in q_object.value:
					store_obj.add_item(i)
		
		elif q_object.operation == "CONTAINS":
			if q_object.field == "name":
				for i in self.store_item:
					if (i.name.__contains__(q_object.value)):
						store_obj.add_item(i)
			else:
				for i in self.store_item:
					if (i.category.__contains__(q_object.value)):
						store_obj.add_item(i)
					
		return store_obj
		
	def exclude(self, q_object):
		store_obj = Store()
		if q_object.operation == "EQ":
			for i in self.store_item:
				if (q_object.value != i.name and q_object.value != i.price and q_object.value != i.category):
					store_obj.add_item(i)
		
		elif q_object.operation == "GT":
			for i in self.store_item:
				if not(q_object.value < i.price):
					store_obj.add_item(i)
		
		elif q_object.operation == "GTE":
			for i in self.store_item:
				if not(q_object.value <= i.price):
					store_obj.add_item(i)
		
		elif q_object.operation == "LT":
			for i in self.store_item:
				if not(q_object.value > i.price):
					store_obj.add_item(i)
		
		elif q_object.operation == "LTE":
			for i in self.store_item:
				if not(q_object.value >= i.price):
					store_obj.add_item(i)
		
		elif q_object.operation == "STARTS_WITH":
			for i in self.store_item:
				if not(i.name.startswith(q_object.value)or i.category.startswith(q_object.value)):
					store_obj.add_item(i)
		
		elif q_object.operation == "ENDS_WITH":
			for i in self.store_item:
				if not(i.name.endswith(q_object.value) or i.category.endswith(q_object.value)):
					store_obj.add_item(i)
		
		elif q_object.operation == "IN":
			for i in self.store_item:
				if not(i.name in q_object.value or i.category in q_object.value or i.price in q_object.value):
					store_obj.add_item(i)
		
		elif q_object.operation == "CONTAINS":
			if q_object.field == "name":
				for i in self.store_item:
					if not(i.name.__contains__(q_object.value)):
						store_obj.add_item(i)
			else:
				for i in self.store_item:
					if not(i.category.__contains__(q_object.value)):
						store_obj.add_item(i)
					
		return store_obj
		
		
class Item:
	def __init__(self, name=None, price=0, category=None):
		self.name = name
		self.price = price
		self.category = category
		#raise error for value
		if price <= 0:
			raise ValueError('Invalid value for price, got {}'.format(price))
	
	def __str__(self):
		return f'{self.name}@{self.price}-{self.category}'
		
class Query:
	valid_op = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
	def __init__(self, field=None, operation=None, value=None):
		self.field = field
		self.operation = operation
		self.value = value
		if operation not in Query.valid_op:
			raise ValueError('Invalid value for operation, got {}'.format(operation))
		
	def __str__(self):
		return f"{self.field} {self.operation} {self.value}"
