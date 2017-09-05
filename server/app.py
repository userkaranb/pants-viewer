"""The flask apps entry point, and all listed routes"""
from flask import Flask, render_template, jsonify
from services.ProductCachingService import ProductCachingService
from data.DataAccess import DataAccess
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)

@APP.route("/")
def root():
    """A Template displaying the list of routes"""
    return render_template('index.html')

@APP.route("/products_with_inventory")
def products_with_inventory():
    """Displays each product, and its inventory"""
    try:
        return jsonify(get_product_caching_service().jsonified_map)
    except Exception as exception:
        return jsonify({'Something went wrong ': exception})

@APP.route("/products")
def products():
    """Displays all products, and product metadata"""
    try:
        return jsonify(get_product_caching_service().jsonofied_product_map)
    except Exception as exception:
        return jsonify({'Something went wrong: ': exception})


@APP.route("/products/<product_id>")
def products_by_id(product_id):
    """Displays inventory for a product id"""
    try:
        return jsonify(get_product_caching_service().jsonified_map[int(product_id)])
    except Exception as exception:
        return jsonify({
            'Something went wrong. Are you sure product '+ product_id + ' exists?': str(exception)
        })

def get_product_caching_service():
    """Returns config product caching service"""
    return APP.config['ProductCachingService']

if __name__ == "__main__":
    APP.config['ProductCachingService'] = ProductCachingService(DataAccess())
    APP.run()
