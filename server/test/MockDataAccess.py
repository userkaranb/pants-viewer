class MockDataAccess(object):
    def __init__(self, mock_product_rows):
        self.mock_product_rows = mock_product_rows

    def get_all_product_rows(self):
        return self.mock_product_rows
