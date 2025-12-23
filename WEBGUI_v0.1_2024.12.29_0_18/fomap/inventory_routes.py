from flask import Blueprint, render_template

inventory_routes = Blueprint('inventory_routes', __name__)

@inventory_routes.route('/')
def inventory():
    return render_template('inventory.html')

@inventory_routes.route('/products')
def products():
    return render_template('products.html')