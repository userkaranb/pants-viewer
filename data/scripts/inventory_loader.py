import MySQLdb
import os

from ProductCsvTranslator import InventoryCsvTranslator

dir_path = os.path.dirname(os.path.realpath(__file__))

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='pants123',
    db='Pants')

cursor = mydb.cursor()
i = InventoryCsvTranslator()
translated_rows = i.translate()
q = 'INSERT INTO tbl_inventory(product_id, waist, length, style, count) VALUES("%s", "%s", "%s", "%s", "%s")'
for product_fields in translated_rows:
    cursor.execute(q, (
        product_fields['id'],
        product_fields['waist'], 
        product_fields['length'], 
        product_fields['style'],
        product_fields['count']
        )   
    )
    mydb.commit()

cursor.close()