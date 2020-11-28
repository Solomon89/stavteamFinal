from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email

class HouseHold(FlaskForm):
    dateCreate = DateField("Дата заполнения: ", validators=[DataRequired()])
    #email = StringField("Email: ", validators=[Email()])
    #message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")