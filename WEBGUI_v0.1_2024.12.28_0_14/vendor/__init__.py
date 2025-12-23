# vendor/__init__.py
from flask import Flask
from vendor.routes.contract_routes import contract_bp
from vendor.routes.data_routes import data_bp
from vendor.routes.list_routes import list_bp

def create_app():
    app = Flask(__name__)

    # Make URLs consistent with navigation
    app.register_blueprint(contract_bp, url_prefix='/app/contracts')
    app.register_blueprint(data_bp, url_prefix='/app/data')
    app.register_blueprint(list_bp, url_prefix='/app/lists')

    return app