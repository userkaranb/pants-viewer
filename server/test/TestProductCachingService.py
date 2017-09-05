from nose import with_setup
from test_modules.MockDataAccess import MockDataAccess
from services.ProductCachingService import ProductCachingService
from models.Product import Product

global_vars = { 
    'ProductCachingService': None,
    'ProductHeaders': ['id', 'product_id', 'waist', 'length', 'style', 'count', 'product_id', 'product_name', 'product_image', 'product_description'],
    'ProductData1': (1, 1, 28, 36, 'style 1', 100, 1, ' " Roomy Trousers 1\" " ', 'www.bonobos.com/1', 'Roomy Beige Trousers'),
    'ProductData2': (2, 2, 30, 32, 'style 2', 85, 2, 'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans'),
    'ProductData3': (3, 2, 32, 32, 'style 3', 10, 2, 'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans')
} 

def setup_product_caching_service():
    fake_product_data = [global_vars['ProductHeaders'], global_vars['ProductData1'], global_vars['ProductData2'], global_vars['ProductData3']]
    mock_data_access = MockDataAccess(fake_product_data)
    global_vars['ProductCachingService'] = ProductCachingService(mock_data_access)

def teardown_product_caching_service():
    global_vars['ProductCachingService'] = None

@with_setup(setup_product_caching_service, teardown_product_caching_service)
def test_initialize_product_map():
    product_caching_service = global_vars['ProductCachingService']
    product_map = product_caching_service.product_map
    assert len(product_map) == 2
    assert 1 in product_map
    assert 2 in product_map
    assert isinstance(product_map[1], Product)

@with_setup(setup_product_caching_service, teardown_product_caching_service)
def test_product_map_to_jsonified_dict():
    product_caching_service = global_vars['ProductCachingService']
    jsonofied_product_map = product_caching_service.jsonofied_product_map
    assert len(jsonofied_product_map) == 2
    assert 1 in jsonofied_product_map
    assert 2 in jsonofied_product_map
    assert isinstance(jsonofied_product_map, dict)
    assert 'inventory_list' not in jsonofied_product_map[1]

@with_setup(setup_product_caching_service, teardown_product_caching_service)
def test_product_map_to_jsonified_dict_with_inventory_list():
    product_caching_service = global_vars['ProductCachingService']
    jsonified_map = product_caching_service.jsonified_map
    assert len(jsonified_map) == 2
    assert 1 in jsonified_map
    assert 2 in jsonified_map
    assert isinstance(jsonified_map, dict)
    assert 'inventory_list' in jsonified_map[2]
    assert len(jsonified_map[2]['inventory_list']) == 2
    assert len(jsonified_map[1]['inventory_list']) == 1
