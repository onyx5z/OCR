# vendor/routes/__init__.py
try:
    from .contract_routes import contract_bp
    from .data_routes import data_bp
    from .list_routes import list_bp
except ImportError as e:
    print(f"Import error: {e}")

__all__ = ['contract_bp', 'data_bp', 'list_bp']