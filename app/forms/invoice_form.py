from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class InvoiceForm(FlaskForm):
    # General invoice details
    invoice_number = StringField('Invoice Number', validators=[DataRequired()])
    invoice_date = DateField('Invoice Date', validators=[DataRequired()])
    existing_supplier = SelectField('Existing Supplier', choices=[], validators=[Optional()]) 
    new_supplier_name = StringField('New Supplier Name', validators=[Optional()])  
    
    # Product fields
    existing_product = SelectField('Existing Product', choices=[], validators=[Optional()])  # Allow for existing product
    new_product_name = StringField('New Product Name', validators=[Optional()])  # Allow for a new product name if product doesn't exist
    quantity_received = IntegerField('Quantity Received', validators=[DataRequired(), NumberRange(min=1)])
    unit_price = FloatField('Unit Price', validators=[DataRequired(), NumberRange(min=0)])
    total_price = FloatField('Total Price', validators=[Optional()])
    
    # Optional additional information
    delivery_date = DateField('Delivery Date', validators=[Optional()])
    notes = TextAreaField('Additional Comments/Notes', validators=[Optional()])
    
    submit = SubmitField('Add Invoice')
