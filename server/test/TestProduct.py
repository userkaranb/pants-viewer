from models.Product import Product
from models.InventoryItem import InventoryItem

def test_product():
    product_id = 3

    waist1 = 30
    length1 = 32
    style1 = 'style 23'
    count1 = 250

    waist2 = 32
    length2 = 34
    style2 = 'style 24'
    count2 = 100

    product_name = 'Big Pants'
    product_image = 'www.bonobos.com/images/13'
    product_description = 'Very large comfy pants'
    
    inventory_item1 = InventoryItem(waist1, length1, style1, count1)
    inventory_item2 = InventoryItem(waist2, length2, style2, count2)
    
    product = Product(product_id, product_name, product_image, product_description, [inventory_item1, inventory_item2])

    assert product.product_id == product_id
    assert product.product_name == product_name
    assert product.product_image == product_image
    assert product.product_description == product_description

    assert len(product.inventory_list) == 2