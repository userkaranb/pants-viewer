"""Translators from CSV files to objects"""
import csv
from abc import ABCMeta, abstractmethod

class BaseCsvTranslator(object):
    """The Base Class that translates csv files to python friendly objects"""
    __metaclass__ = ABCMeta

    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv

    def translate(self):
        """Translate each row from a csv file to list of dictionaries"""
        csv_data = csv.reader(file(self.path_to_csv))
        _ = next(csv_data)
        all_rows = []
        for row in csv_data:
            all_rows.append(self.translate_row(row))
        return all_rows

    @staticmethod
    def format_string(unformatted_str):
        """Return a string without the garbage characters in the csv string"""
        return unformatted_str.replace("'", "").replace("\"", "").replace("\"", "").strip()

    @abstractmethod
    def translate_row(self, row):
        """Given the type of translator, takes a csv row and translates to dictionary"""
        pass

class ProductCsvTranslator(BaseCsvTranslator):
    """Translate the products.csv file into Dictionaries for db insertion"""
    def translate_row(self, row):
        product_id = int(row[0])
        name = row[1]
        image = row[2]
        description = ''.join(row[3:])
        return {
            'id' : product_id,
            'name': self.format_string(name),
            'image': self.format_string(image),
            'description': self.format_string(description)
        }

class InventoryCsvTranslator(BaseCsvTranslator):
    """Translate the inventory.csv file into Dictionaries for db insertion"""
    def translate_row(self, row):
        product_id = int(row[0])
        waist = int(row[1])
        length = int(row[2])
        style = row[3]
        count = int(row[4])
        return {
            'id': product_id,
            'waist': waist,
            'length': length,
            'style': self.format_string(style),
            'count': count
        }
