from flask_wtf import FlaskForm, Form
from wtforms import widgets, StringField, SubmitField, TextAreaField, DateField, \
    SelectField, RadioField, \
    BooleanField, SelectMultipleField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email
from app import dbFunctions


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


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
    waterTime = RadioField(
        'Если в доме нет системы водоснабжения, сколько времени требуется для доставки воды (включая время, '
        'затрачиваемое на то, чтобы добраться до источника, набрать воды и вернуться обратно)',
        choices=dbFunctions.getWaterTime())
    properties = MultiCheckboxField('Наличие собственности следующих типов (отметить все соответствующие окошки)',
                                    choices=dbFunctions.getProperties())
    incoming = FloatField('Текущий средний ежемесячный доход домашнего хозяйства (руб)')
    moneyFoodForHouseHold = FloatField('Сколько денег в месяц тратится на пищу для домашнего хозяйства?')
    hasCult = BooleanField('Есть ли в домашнем хозяйстве пригодная для обработки земля? (в т.ч. дачный участок)')
    cultSquare = FloatField('Какова площадь пригодной для обработки земли в составе домашнего хозяйства?')
    units = RadioField(choices=dbFunctions.getUnits())
    coocking = RadioField('Где находится место приготовления пищи? (выбрать один наиболее подходящий вариант)',
                          choices=dbFunctions.getCoockingPlaces())
    ventil = MultiCheckboxField('Если место приготовления пищи внутри дома, то что из следующего там есть?',
                                choices=dbFunctions.getVentilations())
    coockingOutside = IntegerField(
        'В среднем, сколько месяцев в году вы готовите вне дома? (если менее 1, то, пожалуйста, укажите 01)')
    notEnoughFoodNow = RadioField('В настоящее время (в последние 4 недели)',
                                  choices=dbFunctions.getAnswers())
    notEnoughFoodYear = RadioField('В течение последних 5 лет',
                                   choices=dbFunctions.getAnswers())
    notEnoughClothesNow = RadioField('В настоящее время (в последние 4 недели)',
                                     choices=dbFunctions.getAnswers())
    notEnoughClothesYear = RadioField('В течение последних 5 лет',
                                      choices=dbFunctions.getAnswers())
    notEnoughPayNow = RadioField('В настоящее время (в последние 4 недели)',
                                 choices=dbFunctions.getAnswers())
    notEnoughPayYear = RadioField('В течение последних 5 лет',
                                  choices=dbFunctions.getAnswers())
    assets = MultiCheckboxField('Чем (из следующего) владеет ваше домашнее хозяйство?',
                                choices=dbFunctions.getAssets())
    incomingPartForFood = RadioField(
        'Какую часть дохода вашего домашнего хозяйства вы ежемесячно тратите на еду? (выберите один наиболее '
        'подходящий вариант)',
        choices=dbFunctions.getIncomingParts())
    notEnoughForNecessary = BooleanField(
        'Нам не хватает даже на самое необходимое (пищу, коммунальные счета, необходимую одежду, недорогое лечение)')
    necessaryNotExpensive = BooleanField(
        'Мы можем приобретать все самое необходимое, но не можем покупать дорогие товары длительного пользования')
    expensiveSometimes = BooleanField(
        'Время от времени мы можем приобретать дорогие товары длительного пользования')
    expensiveNotVeryExpensive = BooleanField(
        'Мы можем приобретать товары длительного пользования, но не можем приобрести такие вещи как квартиру, дом, '
        'или дорогой автомобиль')
    veryExpensive = BooleanField(
        'Мы способны покупать такие вещи, как дом, квартиру или дорогой автомобиль')
    incomeLevel = RadioField(
        'Как вы оцениваете уровень достатка вашего домашнего хозяйства, по сравнению с другими. Это: (укажите ОДИН наиболее подходящий вариант)',
        choices=dbFunctions.getIncomeLevels())
    typeHousing = RadioField('В каком типе жилья вы проживаете (выберите один наиболее подходящий вариант)?',
                             choices=dbFunctions.getHousingTypes())
    livingRooms = IntegerField('Сколько жилых комнат в вашем домашнем хозяйстве?')
    livingSquare = FloatField('Какова жилая площадь вашего домашнего хозяйства (в квадратных метрах)?')
    # email = StringField("Email: ", validators=[Email()])
    # message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")
