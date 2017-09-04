from models.InventoryItem import InventoryItem
from models.Product import Product
class DatabaseRowToProductTranslator(object):

    @staticmethod
    def translate_rows_to_model(rows):
        product_id_to_product = {}
        for row in rows[1:]:
            product_id, inventory_item = DatabaseRowToProductTranslator.get_inventory_item(row)
            if product_id in product_id_to_product:
                product_id_to_product[product_id].inventory_list.append(inventory_item)
            else:
                product_id_to_product[product_id] = DatabaseRowToProductTranslator.create_new_product(row, inventory_item, product_id)

        return product_id_to_product

    @staticmethod
    def get_inventory_item(row):
        product_id = int(row[1])
        waist = int(row[2])
        length = int(row[3])
        style = DatabaseRowToProductTranslator.format_string(row[4])
        count = int(row[5])
        return (product_id, InventoryItem(waist, length, style, count))

    @staticmethod
    def create_new_product(row, inventory_item, product_id):
        product_name = DatabaseRowToProductTranslator.format_string(row[7])
        product_image = DatabaseRowToProductTranslator.format_string(row[8])
        product_description = DatabaseRowToProductTranslator.format_string(row[9])
        return Product(product_id, product_name, product_image, product_description, [inventory_item])

    @staticmethod
    def format_string(s):
        return s.replace("'", "").replace("\"", "").replace("\"", "").strip()

