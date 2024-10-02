from app import db

class Product(db.Model):
    __tablename__ = 'products'  # Ensure the table name is correct
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=0)

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(100), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    supplier_name = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity_received = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    delivery_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    
    # Define a relationship to Product
    product = db.relationship('Product', backref='invoices', lazy=True)
