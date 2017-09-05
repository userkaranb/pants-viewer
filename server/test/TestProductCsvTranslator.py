from nose import with_setup
from data.ProductCsvTranslator import ProductCsvTranslator, InventoryCsvTranslator, BaseCsvTranslator

GLOBAL_VARS = {
    'ProductCsvTranslator': None,
    'InventoryCsvTranslator': None
}

def setup_product_csv_translator():
    """Sets up ProductCsvTranslator before each test case"""
    GLOBAL_VARS['ProductCsvTranslator'] = ProductCsvTranslator('test/csv/TestProducts.csv')

def setup_inventory_csv_translator():
    """Sets up InventoryCsvTranslator before each test case"""
    GLOBAL_VARS['InventoryCsvTranslator'] = InventoryCsvTranslator('test/csv/TestInventory.csv')

def teardown_product_translator():
    """Tears down ProductCsvTranslator after each test case"""
    GLOBAL_VARS['ProductCsvTranslator'] = None

def teardown_inventory_translator():
    """Tears down InventoryCsvTranslator after each test case"""
    GLOBAL_VARS['InventoryCsvTranslator'] = None

@with_setup(setup_product_csv_translator, teardown_product_translator)
def test_product_csv_translate():
    """Tests ProductCsvTranslator against a fake csv file"""
    translator = GLOBAL_VARS['ProductCsvTranslator']
    result = translator.translate()
    assert len(result) == 2

    product_1 = result[0]
    assert product_1['id'] == 1
    assert product_1['name'] == 'washed chinos'
    assert product_1['image'] == 'http://www.bonobos.com/1'
    assert product_1['description'] == '100% cotton chinos'

    product_2 = result[1]
    assert product_2['id'] == 2
    assert product_2['name'] == 'jetsetter jeans'
    assert product_2['image'] == 'http://www.bonobos.com/2'
    assert product_2['description'] == 'Innovative stretch denim'

@with_setup(setup_product_csv_translator, teardown_product_translator)
def test_format_string():
    """Tests the removal of garbage characters in a string"""
    translator = GLOBAL_VARS['ProductCsvTranslator']
    style = '" This is a style for a pair of Big Pants\". " '
    expected_style = 'This is a style for a pair of Big Pants.'
    actual_style = translator.format_string(style)
    assert actual_style == expected_style

@with_setup(setup_inventory_csv_translator, teardown_inventory_translator)
def test_inventory_csv_translate():
    """Tests InventoryCsvTranslator against a fake csv file"""
    translator = GLOBAL_VARS['InventoryCsvTranslator']
    result = translator.translate()
    assert len(result) == 5

    # Test 2 of the rows
    row1 = result[0]
    assert row1['id'] == 1
    assert row1['waist'] == 28
    assert row1['length'] == 36
    assert row1['style'] == 'jet blues'
    assert row1['count'] == 75

    row3 = result[2]
    assert row3['id'] == 2
    assert row3['waist'] == 28
    assert row3['length'] == 31
    assert row3['style'] == 'stone cutters'
    assert row3['count'] == 72

def test_base_translator():
    """We should not be able to instantiate an abstract class. This test proves that"""
    err = None
    try:
        BaseCsvTranslator('path')
    except TypeError as ex:
        err = ex

    assert err is not None
