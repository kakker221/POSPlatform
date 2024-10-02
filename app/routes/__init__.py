
# app/routes/__init__.py
from .invoice_routes import invoice_routes  # Import the existing blueprint
from .supplier_routes import supplier_routes  # Import the new blueprint

def register_blueprints(app):
    app.register_blueprint(invoice_routes, url_prefix='/invoices')  # Register it here
    app.register_blueprint(supplier_routes, url_prefix='/suppliers')  # Register it here    
