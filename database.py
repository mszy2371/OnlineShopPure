import sqlite3

conn = sqlite3.connect('./sklep internetowy/database.db')

c = conn.cursor()

# c.execute("""CREATE TABLE products(
#     id integer primary key autoincrement,
#     category text,
#     subcategory text,
#     name text,
#     description text,
#     unit text,
#     qty integer,
#     price_netto real,
#     vat_tax real)""")

    



