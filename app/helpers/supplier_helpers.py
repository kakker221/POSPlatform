from app import db
from app.models import Supplier

def get_or_create_supplier(form):
    if form.existing_supplier.data:
        return Supplier.query.get(form.existing_supplier.data)
    elif form.new_supplier_name.data:
        new_supplier = Supplier(
            name=form.new_supplier_name.data,
            representative=form.representative.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data
        )
        db.session.add(new_supplier)
        db.session.commit()
        return new_supplier
    return None