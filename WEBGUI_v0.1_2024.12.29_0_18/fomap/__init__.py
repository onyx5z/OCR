from flask import Flask


def create_app():
    app = Flask(__name__)

    # Load configurations (optional)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import and register main routes, azért nincs url prefix hogy egyből ezt
    #dobja be
    from .main_routes import main_routes
    app.register_blueprint(main_routes)

    # Import and register dashboard routes
    from .dashboard_routes import dashboard_routes
    app.register_blueprint(dashboard_routes, url_prefix='/dashboard')

    # Import and register inventory routes
    from .inventory_routes import inventory_routes
    app.register_blueprint(inventory_routes, url_prefix='/inventory')

    return app