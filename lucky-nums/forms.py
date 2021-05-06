from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, BooleanField, StringField, FieldList
from wtforms.validators import InputRequired


class InfoForm(FlaskForm):
    name= StringField("Name", validators=[InputRequired()])
    email= StringField("Email", validators=[InputRequired()])
    year= IntegerField("Birth Year", validators=[InputRequired()])
    color= SelectField("Color", choices=[('red', 'Red'), ('green','Green'), ('orange', 'Orange'), ('blue', 'Blue')], validators=[InputRequired()])