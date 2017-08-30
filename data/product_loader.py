import csv
import MySQLdb
import os

from ProductCsvTranslator import ProductCsvTranslator

dir_path = os.path.dirname(os.path.realpath(__file__))

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='pants123',
    db='Pants')

cursor = mydb.cursor()
p = ProductCsvTranslator()
translated_rows = p.translate()
q = 'INSERT INTO tbl_products(product_name, product_image, product_description) VALUES("%s", "%s", "%s")'
for product_id, product_fields in translated_rows.iteritems():
    cursor.execute(q, (product_fields['name'], product_fields['image'], product_fields['description']))
    mydb.commit()

cursor.close()