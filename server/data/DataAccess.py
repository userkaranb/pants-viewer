import sqlite3

class DataAccess(object):
    def __init__(self):
        conn = sqlite3.connect('data/pants.db')
        self.cursor = conn.cursor()

    def query(self):
        q = '''SELECT * FROM inventory AS i INNER JOIN products AS p on i.product_id = p.product_id;'''
        return q

    def get_all_product_rows(self):
        result = []
        self.cursor.execute(self.query())
        field_names = [i[0] for i in self.cursor.description]
        result.append(field_names)
        for row in self.cursor:
            result.append(row)
        return result




