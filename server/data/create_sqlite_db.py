import sqlite3
from ProductCsvTranslator import ProductCsvTranslator, InventoryCsvTranslator
import os

def create_products(c):
    c.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER,
    product_name TEXT,
    product_image TEXT,
    product_description TEXT,
    PRIMARY KEY (product_id)); ''')

def create_inventory(c):
    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER primary key autoincrement,
        product_id INTEGER,
        waist INTEGER,
        length INTEGER,
        style TEXT,
        count INTEGER,
        CONSTRAINT fk_product_id
          FOREIGN KEY (product_id) 
          REFERENCES products(product_id) 
          ON UPDATE CASCADE 
          ON DELETE CASCADE);'''
    )

def insert_products_query():
    return '''INSERT INTO products(product_id, product_name, product_image, product_description) VALUES(?, ?, ?, ?)'''

def insert_inventory_query():
    return '''INSERT INTO inventory(product_id, waist, length, style, count) VALUES(?, ?, ?, ?, ?)'''

def insert_products(c, conn):
    p = ProductCsvTranslator()
    q = insert_products_query()
    translated_rows = p.translate()
    for product_fields in translated_rows:
        c.execute(q, (
            int(product_fields['id']), 
            str(product_fields['name']), 
            str(product_fields['image']), 
            str(product_fields['description'])
            )
        )
        conn.commit()

def insert_inventory(c, conn):
    i = InventoryCsvTranslator()
    q = insert_inventory_query()
    translated_rows = i.translate()
    for product_fields in translated_rows:
        c.execute(q, (
            int(product_fields['id']),
            int(product_fields['waist']),
            int(product_fields['length']), 
            str(product_fields['style']),
            int(product_fields['count'])
            )
        )
        conn.commit()

conn = sqlite3.connect('pants.db')
conn.text_factory = str
c = conn.cursor()
create_products(c)
create_inventory(c)
insert_products(c, conn)
insert_inventory(c, conn)
c.close()