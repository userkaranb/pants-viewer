from flask import Flask, render_template, jsonify
from services.ProductCachingService import ProductCachingService
from data.DataAccess import DataAccess
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/products_with_inventory")
def products_with_inventory():
    return jsonify(product_caching_service.jsonified_map)

@app.route("/products")
def products():
    return jsonify(product_caching_service.jsonofied_product_map)

@app.route("/products/<product_id>")
def products_by_id(product_id):
    return jsonify(product_caching_service.jsonified_map[int(product_id)])

if __name__ == "__main__":
    product_caching_service = ProductCachingService(DataAccess())
    app.run()