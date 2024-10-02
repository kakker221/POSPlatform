from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class SupplierForm(FlaskForm):
    name = StringField('Supplier Name', validators=[DataRequired()])
    address = StringField('Address', validators=[Optional()])
    phone_number = StringField('Phone Number', validators=[Optional()])
    email = StringField('Email', validators=[Optional()])
    submit = SubmitField('Add Supplier')