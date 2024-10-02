# app/routes/invoice_routes.py

from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Product, Invoice
from app import db  # Import db here
from app.models import Product, Invoice  # Import models here
from app.forms.invoice_form import InvoiceForm  # Import form here

invoice_routes = Blueprint('invoices', __name__)

@invoice_routes.route('/add_invoice', methods=['GET', 'POST'])
def add_invoice():
    form = InvoiceForm()

    # Populate product choices from existing products in the system
    form.existing_product.choices = [(product.id, product.name) for product in Product.query.all()]

    if form.validate_on_submit():
        # Check if the user selected an existing product or entered a new product
        if form.existing_product.data:
            # Retrieve the product from the database (existing product)
            product = Product.query.get(form.existing_product.data)
        elif form.new_product_name.data:
            # If the product does not exist, create a new product
            product = Product(
                name=form.new_product_name.data,
                stock=form.quantity_received.data  # Initialize stock with received quantity
            )
            db.session.add(product)
            db.session.commit()  # Commit the new product to get its ID
        else:
            # Handle the case where neither product selection nor new product is provided
            return render_template('add_invoice.html', form=form, error="Please select or add a product.")

        # Update the product's stock based on quantity received
        product.stock += form.quantity_received.data

        # Create a new invoice record
        new_invoice = Invoice(
            invoice_number=form.invoice_number.data,
            invoice_date=form.invoice_date.data,
            supplier_name=form.supplier_name.data,
            product_id=product.id,  # Link the product ID (whether new or existing)
            quantity_received=form.quantity_received.data,
            unit_price=form.unit_price.data,
            total_price=form.unit_price.data * form.quantity_received.data,
            delivery_date=form.delivery_date.data,
            notes=form.notes.data
        )

        # Save changes to the database
        db.session.add(new_invoice)
        db.session.commit()

        return redirect(url_for('invoices.view_invoices'))  # Redirect to invoice listing page (assuming it exists)

    return render_template('add_invoice.html', form=form)
