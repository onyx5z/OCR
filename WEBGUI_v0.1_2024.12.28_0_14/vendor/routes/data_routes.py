# vendor/routes/data_routes.py
from flask import Blueprint, render_template

data_bp = Blueprint('data', __name__)

@data_bp.route('/')
def get_data():
    return render_template('vendor/data.html')