import sqlite3


class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()

    def create_table(self, sql: str):
        self.c.execute(sql)
        self.conn.commit()

    def create_prod_list(self, table_name):
        products = self.c.execute(f"SELECT * FROM {table_name}")
        return products

    def __del__(self):
        self.c.close()

db = Database("database.db")

# db.create_table("""create table products (
#     id integer primary key,
#     name text not null,
#     description text,
#     unit text not null,
#     qty real,
#     purchase_price real,
#     vat_tax real,
#     category text,
#     foreign key (category) references categories(name)
# )"""
# )

# db.create_table("create table categories (name text not null)")
