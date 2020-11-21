import csv




class Category():


    categories = set()
    subcategories = dict()
    with open('products.csv', 'r') as f:
        products_file = csv.DictReader(f)
        for row in products_file:
            categ = row['category']
            sub = row['subcategory']
            categories.add(categ)
            subcategories[categ] = []
            if categ == subcategories[categ]:
            	subcategories[categ].values.append(sub)
            

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
        while category not in cls.categories:
            category = input(f"""Enter product category (chooose existing category
        {cls.categories} or type a new one): """)
            if category in cls.categories:
                break
            print(f"Category does not exist yet. Current categories are: {cls.categories}")
            answer = input(f"Do you want to add a new category? (y/n)")
            if answer.lower() in ('y', 'yes'):
                new_category = category
                print(f"added new category  {new_category}")
                cls.categories.add(new_category)
                break
        subcategory = input("Enter subcategory: ")
        name = input("Enter name: ")
        description = input("Enter description: ")
        unit = input("Enter units: ")
        qty = int(input("Enter qty: "))
        price_netto = float(input("Enter price netto: "))
        vat_tax = float(input("Enter tax threshold: "))
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


#pr_list = Product.prod_list_from_csv('products.csv')

#print(pr_list)



categories = list()
subcategories = dict()

with open('products.csv', 'r') as f:
    products_file = csv.reader(f)
    for row in products_file:
        	if row[0] not in categories:
        		categories.append(row[0])
        		subcategories[row[0]] = []
        	for k, v in subcategories.items():
        	    if k == row[0]:
        	    	if row[1] not in subcategories[row[0]]:
        	    		subcategories[row[0]].append(row[1])

print(categories)
print(subcategories)





