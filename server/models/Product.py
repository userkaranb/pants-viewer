"""Model representing a row in the product csv"""
class Product(object): 
    """A Single Product"""
    def __init__(self, product_id, product_name, product_image, product_description, inventory_list=[]):
        self.product_id = product_id
        self.product_name = product_name
        self.product_image = product_image
        self.product_description = product_description
        self.inventory_list = inventory_list
