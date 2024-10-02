from app import db
from app.models import Product, Invoice

def get_or_create_product(form):
    if form.existing_product.data:
        return Product.query.get(form.existing_product.data)
    elif form.new_product_name.data:
        new_product = Product(
            name=form.new_product_name.data,
            stock=form.quantity_received.data  # Initialize stock
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product
    return None

def create_invoice(form, product):
    new_invoice = Invoice(
        invoice_number=form.invoice_number.data,
        invoice_date=form.invoice_date.data,
        supplier_name=form.supplier_name.data,
        product_id=product.id,
        quantity_received=form.quantity_received.data,
        unit_price=form.unit_price.data,
        total_price=form.unit_price.data * form.quantity_received.data,
        delivery_date=form.delivery_date.data,
        notes=form.notes.data
    )
    return new_invoice
