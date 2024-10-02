
# app/routes/__init__.py
from .invoice_routes import invoice_routes  # Import the existing blueprint

def register_blueprints(app):
    app.register_blueprint(invoice_routes, url_prefix='/invoices')  # Register it here
