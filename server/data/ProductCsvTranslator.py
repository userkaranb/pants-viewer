import csv
import os
from abc import ABCMeta, abstractmethod

class BaseCsvTranslator(object):
    __metaclass__ = ABCMeta

    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv

    def translate(self):
        csv_data = csv.reader(file(self.path_to_csv))
        _ = next(csv_data)
        all_rows = []
        for row in csv_data:
            all_rows.append(self.translate_row(row))
        return all_rows

    def format_string(self, s):
        return s.replace("'", "").replace("\"", "").replace("\"", "").strip()

    @abstractmethod
    def translate_row(row):
        pass

class ProductCsvTranslator(BaseCsvTranslator):
    def __init__(self, path_to_csv = 'csv/products.csv'):
        super(ProductCsvTranslator, self).__init__(path_to_csv)

    def translate_row(self, row):
        id = int(row[0])
        name = row[1]
        image = row[2]
        description = ''.join(row[3:])
        return {
            'id' : id,
            'name': self.format_string(name),
            'image': self.format_string(image),
            'description': self.format_string(description)
        }

class InventoryCsvTranslator(BaseCsvTranslator):
    def __init__(self, path_to_csv = 'csv/inventory.csv'):
        super(InventoryCsvTranslator, self).__init__(path_to_csv)

    def translate_row(self, row):
        id = int(row[0])
        waist = int(row[1])
        length = int(row[2])
        style = row[3]
        count = int(row[4])
        return {
            'id': id,
            'waist': waist,
            'length': length,
            'style': self.format_string(style),
            'count': count
        }