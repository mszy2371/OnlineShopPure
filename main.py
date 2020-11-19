from abc import ABC, abstractmethod
import csv




home = []
office = []
books = []
for_kids = []

categories = ['home', 'office', 'books', 'for_kids']


class Product():

    tax_thresholds = [0, 0.05, 0.08, 0.23]


    def __init__(self, category, subcategory, name, description, unit, qty, price_netto, vat_tax):
        self.category = category
        self.subcategory = subcategory
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
price netto: {self.price_netto}
price inc. tax: {self.price_brutto} per {self.unit}
Quantity in stock: {self.qty} """)



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




def add_product():
    category = False
    while category not in categories:
        category = input(f"""Enter product category (chooose existing category
     {categories} or type a new one): """)
        if category in categories:
            break
        print(f"Category does not exist yet. Current categories are: {categories}")
        answer = input(f"Do you want to add a new category? (y/n)")
        if answer.lower() in ('y', 'yes'):
            new_category = category
            print(f"added new category  {new_category}")
            categories.append(new_category)
            break
    subcategory = input("Enter subcategory: ")
    name = input("Enter name: ")
    description = input("Enter description: ")
    unit = input("Enter units: ")
    qty = int(input("Enter qty: "))
    price_netto = float(input("Enter price netto: "))
    vat_tax = float(input("Enter tax threshold: "))
    product = (category, subcategory, name, description, unit, qty, price_netto, vat_tax)
    with open('./sklep internetowy/products.csv', mode='a') as products_file:
        products_writer = csv.writer(products_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        products_writer.writerow(product)
    return product



product1 = Product(home, "Furniture", "desk", "dark oakwood desk", "item(s)", 25, 350, 0.23)
product2 = Product(home, "Accessories", "picture frame", "pink picture frame", "item(s)", 50, 2.50, 0.23)
product3 = Product(office, "Stationary", "pencils", "HB Pencils with rubber - 12 in box", "box", 120, 1.20, 0.08)

customer1 = Company("Circus Ltd.", "12, Enfield Rd, Potters Bar, EN5 5BE", "office@circus.co.uk", "24354657")
customer2 = Individual("Marcin Szymanek", "94, Mountview Ave, Dunstable, LU5 4DT", "marcin@yahoo.com")


products = []


with open('./sklep internetowy/products.csv', mode='r') as f:
    products_reader = csv.reader(f)
    for row in products_reader:
        prod = Product(*row)
        products.append(prod)


for product in products:
    print(product)
    print()


