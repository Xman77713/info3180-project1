from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired

class AddNewProperty(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    num_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    num_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    p_type = SelectField('Property Type', validate_choice=[InputRequired()] choices=[InputRequired()],
                         choices=[("h", "House"), ("a", "Appartment")])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'jfif', 'webp'])])
    submit = SubmitField('Add Property')