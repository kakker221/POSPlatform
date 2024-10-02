from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Supplier
from app import db
from app.forms.supplier_form import SupplierForm 
from app.helpers.supplier_helpers import get_or_create_supplier

supplier_routes = Blueprint('suppliers', __name__)

@supplier_routes.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    form = SupplierForm()

    if form.validate_on_submit():
        # Get or create the supplier
        supplier = get_or_create_supplier(form)

        if not supplier:
            # If no supplier was selected or entered, return error message and render the form again
            return render_template('add_supplier.html', form=form, error="Please select or add a supplier.")
        
        # Redirect to the supplier list or success page
        return redirect(url_for('suppliers.view_suppliers'))

    # If it's a GET request or form validation fails, render the form
    return render_template('add_supplier.html', form=form)