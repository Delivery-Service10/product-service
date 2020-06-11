from flask import Blueprint, request, jsonify
from models import db, Product
import helper_functions

product_api = Blueprint('product_api', __name__)


@product_api.route("/product/", methods=['POST'])
def create_product():
    data = request.get_json()
    product = helper_functions.populate_product(data)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'product created'})


@product_api.route('/product/id/<public_id>/', methods=['GET'])
def get_one_product(public_id):
    product = Product.query.filter_by(public_id=public_id).first()
    if not product:
        return jsonify({'message': ' No product found'})
    else:
        product_data = helper_functions.allocate_data(product)
        return jsonify({'product': product_data})


@product_api.route('/product/category/<category>/', methods=['GET'])
def get_product_from_category(category):

    products = Product.query.filter_by(category=category)
    return jsonify({'products': helper_functions.combine_results(products)})


@product_api.route('/product/keyword/<keyword>/', methods=['GET'])
def get_specified_products(keyword):

    products = Product.query.filter(Product.name.like("%" + keyword + "%"))
    return jsonify({'drivers': helper_functions.combine_results(products)})


@product_api.route('/product/<public_id>/', methods=['DELETE'])
def delete_product(public_id):
    product = Product.query.filter_by(public_id=public_id).first()
    if not product:
        return jsonify({'message': 'Product not found'})
    else:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted'})
