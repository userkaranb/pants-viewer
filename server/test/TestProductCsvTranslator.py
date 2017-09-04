from nose import with_setup
from data.ProductCsvTranslator import ProductCsvTranslator, InventoryCsvTranslator

global_vars = { 
    'ProductCsvTranslator': None,
    'InventoryCsvTranslator': None
}

def setup_product_csv_translator():
    global_vars['ProductCsvTranslator'] = ProductCsvTranslator('TestProductCsvTranslator.csv')

def setup_inventory_csv_translator():
    global_vars['InventoryCsvTranslator'] = ProductCsvTranslator('TestInventoryCsvTranslator.csv')

def teardown_product_translator():
    global_vars['ProductCsvTranslator'] = None

def teardown_inventory_translator():
    global_vars['InventoryCsvTranslator'] = None
