from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectField, RadioField
from wtforms.validators import DataRequired, Email
from app import dbFunctions

class HouseHold(FlaskForm):
    dateCreate = DateField("Дата заполнения: ", validators=[DataRequired()])
    roofType= RadioField('1. Тип крыши главного дома (выбрать только один вариант)',choices=dbFunctions.getRoofTypes())
    #email = StringField("Email: ", validators=[Email()])
    #message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")