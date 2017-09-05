"""Inventory Item model"""
class InventoryItem(object):
    """A Single Inventory Item"""
    def __init__(self, waist, length, style, count):
        self.waist = waist
        self.length = length
        self.style = style
        self.count = count
