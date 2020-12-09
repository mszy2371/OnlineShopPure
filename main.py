from database import Database, db


class Category:

	def __init__(self, name):
		self.name = name
		self.products = []

	def add_product(self, prod):
		if prod.category is None:
			self.products.append(prod)
			prod.category = self.name
		else:
			print(f"Cannot add product: {prod.name} to category: {self.name}. Product already belongs to category: {prod.category}")
			
	def change_prod_category(self, prod):
		pass
	
	

class Product:

	tax_thresholds = [0, 0.05, 0.08, 0.23]

	counter = 1

	def __init__(self, name, description, unit, qty, purchase_price, vat_tax):
		self.id = Product.counter
		Product.counter += 1
		self.name = name
		self.description = description
		self.unit = unit
		self.qty = int(qty)
		self.purchase_price = float(purchase_price)
		self.price_netto = (self.purchase_price * 1.25).__round__(2)
		self.vat_tax = vat_tax
		self.price_brutto = float(float(self.price_netto) + float(self.price_netto) * float(self.vat_tax)).__round__(2)
		self.category = None


	def __repr__(self):
		return (f"ID:{self.id} product:{self.name} price netto:{self.price_netto} qty: {self.qty}")
	
	def __str__(self):
		return(f"""
Product ID: {self.id}
Product: {self.name}
description: {self.description}
category: 
subcategory: 
price netto: {self.price_netto}
price inc. tax: {self.price_brutto} per {self.unit}
Quantity in stock: {self.qty} """)
	
	def __hash__(self):
		return hash(self.id)
	
	@classmethod
	def prod_list_from_database(cls):
		pass

	@classmethod
	def add_product(cls):
		pass

	def delete_product(self):
		db.c.execute("DELETE FROM products WHERE id=?", (self.id,))


	def order_product(self, qty):
		pass

	def sell_product(self, qty):
		pass



class Customer:
	def __init__(self, name, address, email):
		self.name = name
		self.address = address
		self.email = email
	
	def __str__(self):
		return f"""Customer: {self.name} \n address: {self.address} \n e-mail: {self.email}"""

	@classmethod
	def add_customer(cls):
		pass

	

class Company(Customer):
	def __init__(self, name, address, email, tax_no):
		super().__init__(name, address, email)
		self.tax_no = tax_no


class Individual(Customer):
	def __init__(self, name, address, email):
		super().__init__(name, address, email)


class Supplier(Customer):
	pass


prod1 = Product('desk', 'brown oakwood desk', 'item', 8, 134.69, 0.23)
prod2 = Product('chair', 'black office desk chair', 'item', 10, 65.30, 0.23)
prod3 = Product('mug', 'yellow coffee mug', 'item', 110, 2.60, 0.08)
cat1 = Category('office')
cat2 = Category('home')


cat1.add_product(prod1)
cat1.add_product(prod2)
cat2.add_product(prod3)
cat1.add_product(prod3)

print(prod1.category)
print(prod2.category)
print(prod3.category)
print(cat1.products)
print(cat2.products)