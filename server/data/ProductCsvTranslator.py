import csv
import os

class ProductCsvTranslator(object):
    def __init__(self, path_to_csv = 'csv/products.csv'):
        self.path_to_csv = path_to_csv

    def translate(self):
        csv_data = csv.reader(file(self.path_to_csv))
        _ = next(csv_data)
        all_rows = []
        for row in csv_data:
            all_rows.append(self.translate_row(row))
        return all_rows
            
    def translate_row(self, row):
        id = int(row[0])
        name = row[1]
        image = row[2]
        description = ''.join(row[3:])
        return {
            'id' : id,
            'name': name,
            'image': image,
            'description': description
        }

class InventoryCsvTranslator(object):
    def __init__(self, path_to_csv = 'csv/inventory.csv'):
        self.path_to_csv = path_to_csv

    def translate(self):
        csv_data = csv.reader(file(self.path_to_csv))
        _ = next(csv_data)
        all_rows = []
        for row in csv_data:
            all_rows.append(self.translate_row(row))
        return all_rows

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
            'style': style,
            'count': count
        }