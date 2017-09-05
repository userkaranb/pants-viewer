"""A file for keeping repeatedly used mock data for testing"""
from test.test_modules.MockDataAccess import MockDataAccess
class TestHelperData(object):
    """A Collection of static methods that return dummy data"""
    @staticmethod
    def fake_database_rows():
        """Fake rows for a fake database"""
        product_headers = [
            'id',
            'product_id',
            'waist',
            'length',
            'style',
            'count',
            'product_id',
            'product_name',
            'product_image',
            'product_description'
        ]

        product_data_1 = (1, 1, 28, 36, 'style 1', 100, 1, 'Roomy Trousers 1',
                          'www.bonobos.com/1', 'Roomy Beige Trousers')
        product_data_2 = (2, 2, 30, 32, 'style 2', 85, 2,
                          'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans')
        product_data_3 = (3, 2, 32, 32, 'style 3', 10, 2,
                          'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans')
        product_data_4 = (4, 1, 32, 32, 'style 4', 10, 1,
                          'Roomy Trousers 1', 'www.bonobos.com/1', 'Roomy Beige Trousers')
        return [product_headers, product_data_1, product_data_2, product_data_3, product_data_4]

    @staticmethod
    def mock_data_access():
        """Returns a fake data access for testing"""
        return MockDataAccess(TestHelperData.fake_database_rows())
