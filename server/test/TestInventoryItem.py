from models.InventoryItem import InventoryItem

def test_inventory_item():
    waist = 30
    length = 32
    style = 'style 23'
    count = 250
    
    inventory_item = InventoryItem(waist, length, style, count)

    assert inventory_item.waist == waist
    assert inventory_item.length == length
    assert inventory_item.style == style
    assert inventory_item.count == count