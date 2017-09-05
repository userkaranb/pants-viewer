"""Translate database rows to models"""
from models.InventoryItem import InventoryItem
from models.Product import Product
class DatabaseRowToProductTranslator(object):
    """Static class translating a database row to a map, mapping product id to product"""
    @staticmethod
    def translate_rows_to_model(rows):
        """Top level function that returns product id to product model"""
        product_id_to_product = {}
        for row in rows[1:]:
            product_id, inventory_item = DatabaseRowToProductTranslator.get_inventory_item(row)
            if product_id in product_id_to_product:
                product_id_to_product[product_id].inventory_list.append(inventory_item)
            else:
                new_product = DatabaseRowToProductTranslator.create_new_product(
                    row, inventory_item, product_id)
                product_id_to_product[product_id] = new_product

        return product_id_to_product

    @staticmethod
    def get_inventory_item(row):
        """Given a row, get the inventory related data"""
        product_id = int(row[1])
        waist = int(row[2])
        length = int(row[3])
        style = row[4]
        count = int(row[5])
        return (product_id, InventoryItem(waist, length, style, count))

    @staticmethod
    def create_new_product(row, inventory_item, product_id):
        """Create a new product instance"""
        product_name = row[7]
        product_image = row[8]
        product_description = row[9]
        return Product(
            product_id, product_name, product_image, product_description, [inventory_item])
