class Store:
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
	
	def __add__(self,q_object):
		store = Store()
		for items in self.store_item:
			store.add_item(items)
		for items in q_object.store_item:
			store.add_item(items)
		return store
		
	def filter(self, q_object):
		store_obj = Store()
		for items in self.store_item:
			field_name = q_object.field
			if q_object.operation == 'EQ' and getattr(items,field_name) == q_object.value:
				store_obj.add_item(items)
			elif q_object.operation == 'GT' and getattr(items,field_name) > q_object.value:
				store_obj.add_item(items)
			elif q_object.operation == 'GTE' and getattr(items,field_name) >= q_object.value:
				store_obj.add_item(items)
			elif q_object.operation == 'LT' and getattr(items,field_name) < q_object.value:
				store_obj.add_item(items)
			elif q_object.operation == 'LTE' and getattr(items,field_name) <= q_object.value:
				store_obj.add_item(items)
			elif (q_object.operation == 'CONTAINS' or q_object.operation == 'STARTS_WITH' or q_object.operation== 'ENDS_WITH') and q_object.value in getattr(items,field_name):
				store_obj.add_item(items)
			elif q_object.operation == 'IN' and getattr(items,field_name) in q_object.value:
				store_obj.add_item(items)
		return store_obj
		
	def exclude(self, q_object):
		exclude_obj = Store()
		include_obj = self.filter(q_object)
		for items in self.store_item:
			if items not in include_obj.store_item:
				exclude_obj.add_item(items)
		return exclude_obj
		
class Item:
	def __init__(self, name=None, price=0, category=None):
		self._name = name
		self._price = price
		self._category = category
		#raise error for value
		if price <= 0:
			raise ValueError('Invalid value for price, got {}'.format(price))
	
	@property
	def name(self):
		return self._name
	
	@property
	def price(self):
		return self._price
	
	@property
	def category(self):
		return self._category
	
	def __str__(self):
		return f'{self._name}@{self._price}-{self._category}'
		
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
