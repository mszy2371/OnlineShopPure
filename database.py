import sqlite3


class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()

    def create_prod_list(self, table_name):
        products = self.c.execute(f"SELECT * FROM {table_name}")
        return products

    def __del__(self):
        self.c.close()

db = Database("database.db")






    



