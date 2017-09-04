from MockDataAccess import MockDataAccess
from services.ProductCachingService import ProductCachingService
from app import app
import mock
from nose import with_setup
import json

global_vars = { 
    'ProductCachingService': None,
    'ProductHeaders': ['id', 'product_id', 'waist', 'length', 'style', 'count', 'product_id', 'product_name', 'product_image', 'product_description'],
    'ProductData1': (1, 1, 28, 36, 'style 1', 100, 1, ' " Roomy Trousers 1\" " ', 'www.bonobos.com/1', 'Roomy Beige Trousers'),
    'ProductData2': (2, 2, 30, 32, 'style 2', 85, 2, 'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans'),
    'ProductData3': (3, 2, 32, 32, 'style 3', 10, 2, 'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans')
} 

def setup_test_client():
    fake_product_data = [global_vars['ProductHeaders'], global_vars['ProductData1'], global_vars['ProductData2'], global_vars['ProductData3']]
    mock_data_access = MockDataAccess(fake_product_data)
    app.config['ProductCachingService'] = ProductCachingService(mock_data_access)
    tester = app.test_client()
    global_vars['tester'] = tester

def teardown_test_client():
    global_vars['tester'] = None

@with_setup(setup_test_client, teardown_test_client)
def test_products():
    tester = global_vars['tester']
    response = tester.get('/products', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_products_with_inventory():
    tester = global_vars['tester']
    response = tester.get('/products_with_inventory', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_root():
    tester = global_vars['tester']
    response = tester.get('/', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_product_id_1():
    tester = global_vars['tester']
    response = tester.get('/products/1', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_product_id_2():
    tester = global_vars['tester']
    response = tester.get('/products/2', content_type='application/json')
    assert response.status == '200 OK'

@with_setup(setup_test_client, teardown_test_client)
def test_product_id_3():
    tester = global_vars['tester']
    response = tester.get('/products/3', content_type='application/json')
    response_body = str(json.loads(response.response.next()).keys()[0])
    assert response_body == 'Something went wrong. Are you sure product 3 exists?'