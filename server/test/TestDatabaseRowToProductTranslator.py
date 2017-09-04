from nose import with_setup
from models.Product import Product
from models.InventoryItem import InventoryItem
from services.DatabaseRowToProductTranslator import DatabaseRowToProductTranslator

global_vars = { 
    'ProductHeaders': ['id', 'product_id', 'waist', 'length', 'style', 'count', 'product_id', 'product_name', 'product_image', 'product_description'],
    'ProductData1': (1, 1, 28, 36, 'style 1', 100, 1, ' " Roomy Trousers 1\" " ', 'www.bonobos.com/1', 'Roomy Beige Trousers'),
    'ProductData2': (2, 2, 30, 32, 'style 2', 85, 2, 'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans'),
    'ProductData3': (3, 2, 32, 32, 'style 3', 10, 2, 'Skinny Jeans 1', 'www.bonobos.com/2', 'Skinny Jeans'),
    'ProductData4': (4, 1, 32, 32, 'style 4', 10, 1, ' " Roomy Trousers 1\" " ', 'www.bonobos.com/1', 'Roomy Beige Trousers')
}


def setup_fake_data_rows():
    global_vars['fake_data_rows'] = [
        global_vars['ProductHeaders'],
        global_vars['ProductData1'],
        global_vars['ProductData2'],
        global_vars['ProductData3'],
        global_vars['ProductData4']
    ]

def tear_down_fake_data_rows():
    pass

@with_setup(setup_fake_data_rows, tear_down_fake_data_rows)
def test_translate_rows_to_model_product():
    fake_data_rows = global_vars['fake_data_rows']
    result = DatabaseRowToProductTranslator.translate_rows_to_model(fake_data_rows)
    assert set(result.keys()) == set([1,2])
    assert len(result.keys()) == 2
    assert isinstance(result[1], Product)
    assert result[1].product_id == 1
    assert result[1].product_description == 'Roomy Beige Trousers'
    assert result[1].product_image == 'www.bonobos.com/1'
    assert result[1].product_name == 'Roomy Trousers 1'

@with_setup(setup_fake_data_rows, tear_down_fake_data_rows)
def test_translate_rows_to_model_inventory_list():
    fake_data_rows = global_vars['fake_data_rows']
    result = DatabaseRowToProductTranslator.translate_rows_to_model(fake_data_rows)
    inventory_list = result[1].inventory_list
    assert len(inventory_list) == 2
    
    waists = set([inventory_item.waist for inventory_item in inventory_list])
    assert waists == set([28, 32])

    lengths = set([inventory_item.length for inventory_item in inventory_list])
    assert lengths == set([36, 32])

    counts = set([inventory_item.count for inventory_item in inventory_list])
    assert counts == set([100, 10])

    styles = set([inventory_item.style for inventory_item in inventory_list])
    assert styles == set(['style 1', 'style 4'])

def test_get_inventory_item():
    row_id = 10
    product_id = 3
    waist = 40
    length = 45
    style = 'Style 10'
    count = 1000
    row = (row_id, product_id, waist, length, style, count)
    result = DatabaseRowToProductTranslator.get_inventory_item(row)

    assert result[0] == product_id
    assert result[1].waist == waist
    assert result[1].length == length
    assert result[1].style == style
    assert result[1].count == count

def test_create_new_product():
    row_id = 10
    product_id = 3
    waist = 30
    length = 32
    style = 'style 23'
    count = 250
    product_name = 'Big Pants'
    product_image = 'www.bonobos.com/images/13'
    product_description = 'Very large comfy pants'
    inventory_item = InventoryItem(waist, length, style, count)
    row = (row_id, product_id, waist, length, style, count, product_id, product_name, product_image, product_description)
    product_result = DatabaseRowToProductTranslator.create_new_product(row, inventory_item, product_id)

    assert isinstance(product_result, Product)
    assert product_result.product_id == product_id
    assert product_result.product_name == product_name
    assert product_result.product_image == product_image
    assert product_result.product_description == product_description
    
    assert len(product_result.inventory_list) == 1
    assert product_result.inventory_list[0].style == style
    assert product_result.inventory_list[0].waist == waist
    assert product_result.inventory_list[0].length == length
    assert product_result.inventory_list[0].count == count

def test_format_string():
    style = '" This is a style for a pair of Big Pants\". " '
    expected_style = 'This is a style for a pair of Big Pants.'
    actual_style = DatabaseRowToProductTranslator.format_string(style)
    assert actual_style == expected_style