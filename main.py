import csv




class Category():


	categories = dict()
	subcategories = dict()
	with open('products.csv', 'r') as f:
		products_file = csv.reader(f)
		for row in products_file:
			if row[0] not in categories:
				categories[row[0]] = []
			for k, v in categories.items():
				if k == row[0]:
					if row[1] not in v:
						v.append(row[1])
						subcategories[row[1]] = []
			for key, value in subcategories.items():
				if key == row[1]:
					if row[2] not in value:
						value.append(row[2])
	@classmethod
	def list_items(cls, collection):
		items = []
		for item in collection:
			items.append(item)
		return items
			

	def __init__(self, category, subcategory):
		self.category = category
		self.subcategory = subcategory

	

	
	

class Product(Category):

	tax_thresholds = [0, 0.05, 0.08, 0.23]


	def __init__(self, category, subcategory, name, description, unit, qty, price_netto, vat_tax):
		super().__init__(category, subcategory)
		self.name = name
		self.description = description
		self.unit = unit
		self.qty = int(qty)
		self.price_netto = float(price_netto)
		self.vat_tax = vat_tax
		self.price_brutto = float(float(price_netto) + float(price_netto) * float(vat_tax)).__round__(2)

	def __repr__(self):
		return (f"{self.name} - price netto: {self.price_netto}  qty: {self.qty}")
	
	def __str__(self):
		return(f"""Product: {self.name}
description: {self.description}
category: {self.category}
subcategory: {self.subcategory}
price netto: {self.price_netto}
price inc. tax: {self.price_brutto} per {self.unit}
Quantity in stock: {self.qty} """)
	
	@classmethod
	def prod_list_from_csv(cls, file):
		products = list()
		with open(file , mode='r') as f:
			products_reader = csv.reader(f)
			rowNr = 0
			for row in products_reader:
				if rowNr >= 1:
					prod = cls(*row)
					products.append(prod)
				rowNr += 1
		return products

	@classmethod
	def add_product(cls):
		category = False
		subcategory = False
		new_category =False
		while category not in cls.categories:
			category = input(f"""Enter product CATEGORY (chooose one of the existing categories
{cls.list_items(cls.categories)} or type a new one): """)
			if category in cls.categories:
				break
			print(f"Category does not exist yet. Current categories are: {cls.list_items(cls.categories)}")
			answer = input(f"Do you want to add a new category? (y/n)")
			if answer.lower() in ('y', 'yes'):
				new_category = category
				print(f"added new category  {new_category}")
				cls.categories[new_category] = []
				break
		while subcategory not in cls.subcategories:
			if new_category:
				new_subcategory = input(f"Enter a subcategory for product in new category '{new_category}': ")
				subcategory = new_subcategory
				print(f"added new subcategory  {subcategory}")
				cls.subcategories[subcategory] = []
				cls.categories[category].append(cls.subcategories[new_subcategory])
			else:
				subcategory = input(f"""Enter product SUBCATEGORY (chooose existing subcategory {cls.list_items(cls.categories[category])}
				or type a new one): """)
				if subcategory in cls.subcategories:
					break
				else:
					print(f"Subcategory does not exist yet. Current subcategories of category {category} are: {cls.list_items(cls.categories[category])}")
					answer = input(f"Do you want to add a new subcategory? (y/n)")
					if answer.lower() in ('y', 'yes'):
						new_subcategory = subcategory
						print(f"added new subcategory  {new_subcategory}")
						cls.subcategories[new_subcategory] = []
						cls.categories[category].append(cls.subcategories[new_subcategory])
						break
		name = input("Enter product name: ")
		description = input("Enter product description: ")
		unit = input("Enter units (i.e. item, kg, cm etc.): ")
		qty = int(input("Enter quantity: "))
		price_netto = float(input("Enter price netto: "))
		vat_tax = None
		while vat_tax not in cls.tax_thresholds:
			vat_tax = float(input("Enter tax threshold: (available options: 0, 0.05, 0.08 or 0.23): "))
			if vat_tax not in cls.tax_thresholds:
				print("Incorrect tax threshold")
		product = (category, subcategory, name, description, unit, qty, price_netto, vat_tax)
		with open('products.csv', mode='a') as products_file:
			products_writer = csv.writer(products_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			products_writer.writerow(product)
		return product


class Customer:
	def __init__(self, name, address, email):
		self.name = name
		self.address = address
		self.email = email
	
	def __str__(self):
		return f"""Customer: {self.name} \n address: {self.address} \n e-mail: {self.email}"""


class Company(Customer):
	def __init__(self, name, address, email, tax_no):
		super().__init__(name, address, email)
		self.tax_no = tax_no


class Individual(Customer):
	def __init__(self, name, address, email):
		super().__init__(name, address, email)



customer1 = Company("Circus Ltd.", "12, Enfield Rd, Potters Bar, EN5 5BE", "office@circus.co.uk", "24354657")
customer2 = Individual("Marcin Szymanek", "94, Mountview Ave, Dunstable, LU5 4DT", "marcin@yahoo.com")


# products = Product.prod_list_from_csv('products.csv')

# print(products[1])



Product.add_product()



