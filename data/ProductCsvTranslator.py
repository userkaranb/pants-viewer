import csv
import os

class ProductCsvTranslator(object):
    def __init__(self, path_to_csv = 'data/csv/products.csv'):
        self.path_to_csv = path_to_csv

    def translate(self):
        csv_data = csv.reader(file(self.path_to_csv))
        _ = next(csv_data)
        all_rows = {}
        for row in csv_data:
            all_rows.update(self.translate_row(row))
        return all_rows
            
    def translate_row(self, row):
        id = int(row[0])
        name = row[1]
        image = row[2]
        description = ''.join(row[3:])
        return {
            id: {
                'name': name,
                'image': image,
                'description': description
            }
        }
