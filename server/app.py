from flask import Flask, render_template, jsonify
from services.ProductCachingService import ProductCachingService
from data.DataAccess import DataAccess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/products_with_inventory")
def products_with_inventory():
    try:
        return jsonify(get_product_caching_service().jsonified_map)
    except Exception as e:
        return jsonify({'Something went wrong ': e})

@app.route("/products")
def products():
    try:
        return jsonify(get_product_caching_service().jsonofied_product_map)
    except Exception as e:
        return jsonify({'Something went wrong: ': e})


@app.route("/products/<product_id>")
def products_by_id(product_id):
    try:
        return jsonify(get_product_caching_service().jsonified_map[int(product_id)])
    except Exception as e:
         print e
         return jsonify({'Something went wrong. Are you sure product '+ product_id + ' exists?': str(e)})

def get_product_caching_service():
    return app.config['ProductCachingService']

if __name__ == "__main__":
    app.config['ProductCachingService'] = ProductCachingService(DataAccess())
    app.run()