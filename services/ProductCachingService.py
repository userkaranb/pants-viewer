class ProductCachingService(object):
    def __init__(self, dataAccess):
        # Takes data access
        pass

    def initialize_product_map(self):
        # data access gets all rows on join
        # Pass this into translator, which maps product ID to product (containing inventory)
