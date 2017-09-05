"""Gateway module to the sqlite3 database"""
import sqlite3

class DataAccess(object):
    """Gateway class to the sqlite3 database"""
    def __init__(self):
        conn = sqlite3.connect('data/pants.db')
        self.cursor = conn.cursor()

    @staticmethod
    def query():
        """Getting all products and their inventories in one list"""
        return """
                SELECT * FROM inventory AS i 
                INNER JOIN products AS p on i.product_id = p.product_id;
                """

    def get_all_product_rows(self):
        """Returns a list of all rows that match the query"""
        result = []
        self.cursor.execute(self.query())
        field_names = [i[0] for i in self.cursor.description]
        result.append(field_names)
        for row in self.cursor:
            result.append(row)
        return result
