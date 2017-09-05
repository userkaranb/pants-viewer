"""Reading from the database, caching products in memory"""
from services.DatabaseRowToProductTranslator import DatabaseRowToProductTranslator

class ProductCachingService(object):
    """A class that reads from the database, and on creation has several formatted maps"""
    def __init__(self, data_access):
        self.data_access = data_access
        self.product_map = self.initialize_product_map()
        self.jsonofied_product_map = self.product_map_to_jsonified_dict()
        self.jsonified_map = self.map_to_product_inventory()

    def initialize_product_map(self):
        """Returns a map of product id to product"""
        all_rows = self.data_access.get_all_product_rows()
        product_map = DatabaseRowToProductTranslator.translate_rows_to_model(all_rows)
        return product_map

    def product_map_to_jsonified_dict(self):
        """Returns a jsonifiable dictionary mapping product id to product metadata"""
        result = {}
        for product_id, product in self.product_map.iteritems():
            jsonified_product = product.__dict__.copy()
            jsonified_product.pop('inventory_list', None)
            result[product_id] = jsonified_product
        return result

    def map_to_product_inventory(self):
        """Returns a jsonifiable dictionary mapping product id to product metadata and inventory"""
        result = {}
        for product_id, product in self.product_map.iteritems():
            inventory_items = []
            for inventory_item in product.inventory_list:
                inventory_items.append(inventory_item.__dict__)
            jsonified_product = product.__dict__
            jsonified_product['inventory_list'] = inventory_items
            result[product_id] = jsonified_product
        return result
