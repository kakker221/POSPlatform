# app/routes/invoice_routes.py

from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Product, Invoice
from app import db
from app.models import Product, Invoice 
from app.forms.invoice_form import InvoiceForm 
from app.helpers.invoice_helpers import get_or_create_product, create_invoice


invoice_routes = Blueprint('invoices', __name__)

@invoice_routes.route('/add_invoice', methods=['GET', 'POST'])
def add_invoice():
    form = InvoiceForm()

    # Populate existing product choices
    form.existing_product.choices = [(str(product.id), product.name) for product in Product.query.all()]

    if form.validate_on_submit():
        # Get or create the product
        product = get_or_create_product(form)

        if not product:
            # If no product was selected or entered, return error
            return render_template('add_invoice.html', form=form, error="Please select or add a product.")

        # Update the product's stock
        product.stock += form.quantity_received.data
        db.session.commit()  # Commit the updated stock

        # Create the invoice
        new_invoice = create_invoice(form, product)

        # Save the invoice to the database
        db.session.add(new_invoice)
        db.session.commit()

        return redirect(url_for('invoices.view_invoices'))

    return render_template('add_invoice.html', form=form)
