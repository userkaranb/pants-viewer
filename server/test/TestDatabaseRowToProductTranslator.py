"""Test our translator from Database to Model"""
from test.test_modules.TestHelperData import TestHelperData
from models.Product import Product
from models.InventoryItem import InventoryItem
from services.DatabaseRowToProductTranslator import DatabaseRowToProductTranslator

def test_translate_rows_to_product():
    """Translate row to Product test"""
    fake_data_rows = TestHelperData.fake_database_rows()
    result = DatabaseRowToProductTranslator.translate_rows_to_model(fake_data_rows)
    assert set(result.keys()) == set([1, 2])
    assert len(result.keys()) == 2
    assert isinstance(result[1], Product)
    assert result[1].product_id == 1
    assert result[1].product_description == 'Roomy Beige Trousers'
    assert result[1].product_image == 'www.bonobos.com/1'
    assert result[1].product_name == 'Roomy Trousers 1'

def test_translate_rows_to_inv():
    """Translate rows to Product and corresponding inventory lists"""
    fake_data_rows = TestHelperData.fake_database_rows()
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
    """Test the retrieval of inventory item from database"""
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
    """Test creating new product model"""
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
    row = (row_id, product_id, waist,
           length, style, count, product_id, product_name, product_image, product_description)
    product_result = DatabaseRowToProductTranslator.create_new_product(
        row, inventory_item, product_id)

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
