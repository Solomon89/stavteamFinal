from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectField, RadioField, \
    BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Email
from app import dbFunctions

class PropertiesField(Form):
    def __init__(self, *args, **kwargs):
        super(PropertiesField, self).__init__(*args, **kwargs)
        properties=dbFunctions.getProperties()
        for property in properties:
            self.fields['property-{index}'.format(index=property[0])] = \
                BooleanField(property[1])

class HouseHold(FlaskForm):
    dateCreate = DateField("Дата заполнения: ", validators=[DataRequired()], format='%Y-%m-%d')
    roofType = RadioField('Тип крыши главного дома (выбрать только один вариант)', choices=dbFunctions.getRoofTypes())
    electricity = BooleanField('Наличие электричества в доме')
    fuelType = RadioField('Основной тип топлива, используемый для приготовления пищи (выбрать только один вариант)',
                          choices=dbFunctions.getFuelTypes())
    heatType = RadioField('Основной источник теплоснабжения в холодный / дождливый сезон (выбрать только один вариант)',
                          choices=dbFunctions.getHeatTypes())
    waterSource = RadioField('Основной источник питьевой воды (выбрать только один вариант)',
                             choices=dbFunctions.getWaterSources())
    waterTime = RadioField('Если в доме нет системы водоснабжения, сколько времени требуется для доставки воды (включая время, затрачиваемое на то, чтобы добраться до источника, набрать воды и вернуться обратно)',
                           choices=dbFunctions.getWaterTime())
    properties = PropertiesField()
    # email = StringField("Email: ", validators=[Email()])
    # message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")
