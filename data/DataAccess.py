import MySQLdb
class DataAccess(object):
    def __init__(self):
        self.mydb = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='pants123',
            db='Pants'
        )

    def query(self):
        q = 'SELECT * FROM pants.tbl_inventory AS i '\
        'INNER JOIN pants.tbl_products AS p on i.product_id = p.product_id;'
        return q

    def get_all_product_rows(self):
        result = []
        cursor = self.mydb.cursor()
        cursor.execute(self.query())
        field_names = [i[0] for i in cursor.description]
        result.append(field_names)
        for row in cursor:
            result.append(row)
        return result




