"""Tests for our product caching sevice"""
from test.test_modules.TestHelperData import TestHelperData
from nose import with_setup
from services.ProductCachingService import ProductCachingService
from models.Product import Product

GLOBAL_VARS = {
    'ProductCachingService': None
}

def setup_product_caching_service():
    """Set up a ProductCachingService instance before each test case"""
    mock_data_access = TestHelperData.mock_data_access()
    GLOBAL_VARS['ProductCachingService'] = ProductCachingService(mock_data_access)

def tear_product_caching_service():
    """Tear down our just used ProductCachingService after each test case"""
    GLOBAL_VARS['ProductCachingService'] = None

@with_setup(setup_product_caching_service, tear_product_caching_service)
def test_initialize_product_map():
    """Test our cached ProductId to Product map"""
    product_caching_service = GLOBAL_VARS['ProductCachingService']
    product_map = product_caching_service.product_map
    assert len(product_map) == 2
    assert 1 in product_map
    assert 2 in product_map
    assert isinstance(product_map[1], Product)

@with_setup(setup_product_caching_service, tear_product_caching_service)
def test_jsonofied_product_map():
    """Test our cached jsonfiable ProductId to product map"""
    product_caching_service = GLOBAL_VARS['ProductCachingService']
    jsonofied_product_map = product_caching_service.jsonofied_product_map
    assert len(jsonofied_product_map) == 2
    assert 1 in jsonofied_product_map
    assert 2 in jsonofied_product_map
    assert isinstance(jsonofied_product_map, dict)
    assert 'inventory_list' not in jsonofied_product_map[1]

@with_setup(setup_product_caching_service, tear_product_caching_service)
def test_jsonified_map():
    """Test our cached jsonifiable product id to product and inventory map"""
    product_caching_service = GLOBAL_VARS['ProductCachingService']
    jsonified_map = product_caching_service.jsonified_map
    assert len(jsonified_map) == 2
    assert 1 in jsonified_map
    assert 2 in jsonified_map
    assert isinstance(jsonified_map, dict)
    assert 'inventory_list' in jsonified_map[2]
    assert len(jsonified_map[2]['inventory_list']) == 2
    assert len(jsonified_map[1]['inventory_list']) == 2
