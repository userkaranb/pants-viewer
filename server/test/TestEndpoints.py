"""Test the validity of our main endpoints with mocked data access"""
import json
from test.test_modules.TestHelperData import TestHelperData
from services.ProductCachingService import ProductCachingService
from app import APP
from nose import with_setup

GLOBAL_VARS = {
    'ProductCachingService': None
}

def setup_test_client():
    """Set up our test client we will use for endpoint access"""
    mock_data_access = TestHelperData.mock_data_access()
    APP.config['ProductCachingService'] = ProductCachingService(mock_data_access)
    tester = APP.test_client()
    GLOBAL_VARS['tester'] = tester

def teardown_test_client():
    """Tear down our test client"""
    GLOBAL_VARS['tester'] = None

@with_setup(setup_test_client, teardown_test_client)
def test_products():
    """/products should return 200 code"""
    tester = GLOBAL_VARS['tester']
    response = tester.get('/products', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_products_with_inventory():
    """/products_with_inventory should return a 200 code"""
    tester = GLOBAL_VARS['tester']
    response = tester.get('/products_with_inventory', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_root():
    """/ should return a 200 code"""
    tester = GLOBAL_VARS['tester']
    response = tester.get('/', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_product_id_1():
    """/products/1 should return a 200 code"""
    tester = GLOBAL_VARS['tester']
    response = tester.get('/products/1', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_product_id_2():
    """/products/2 should return a 200 code"""
    tester = GLOBAL_VARS['tester']
    response = tester.get('/products/2', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_product_id_3():
    """/products/1 should return an error, product 3 does not exist"""
    tester = GLOBAL_VARS['tester']
    response = tester.get('/products/3', content_type='application/json')
    response_body = str(json.loads(response.response.next()).keys()[0])
    assert response_body == 'Something went wrong. Are you sure product 3 exists?'
