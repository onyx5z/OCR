# vendor/routes/list_routes.py
from flask import Blueprint, render_template, abort

list_bp = Blueprint('list', __name__)

@list_bp.route('/')
def get_lists():
    try:
        return render_template('vendor/list.html')
    except Exception as e:
        app.logger.error(f"Error in get_lists: {str(e)}")
        abort(500)