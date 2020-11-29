from stavteam import app
from flask import render_template
from flask import jsonify, request
from app import dbFunctions
from flask import abort
from flask import render_template
from app import forms
import matplotlib.pyplot as plt
from mpld3 import fig_to_html, plugins
import numpy as np


@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html", user="Stavteam")

@app.route('/houseHold', methods=['POST','GET'])
def houseHold():
    if request.method == 'GET':
        return render_template('houseHold.html', form=forms.HouseHold())


@app.route('/login', methods=['POST'])
def login():
    param = request.get_json()
    sql = '''SELECT public.users.*, public.roles.name  FROM public.users 
             left outer join public.roles on  public.users.roleid= public.roles.id 
             where users.login='%s' ''' % param['userName']
    rows = dbFunctions.execSQL(sql, None, True)
    if len(rows) > 0:
        for row in rows:
            print('password is ', row[5], 'getting ',  param['userPass'])
            if row[5].strip() == param['userPass']:
                uid = dbFunctions.makeSession(row[0])
                userInfo = {'FAM': row[1], 'IM': row[2], 'OT': row[3], 'ROLE':row[7],  'SESSION': uid}
                return jsonify(userInfo)
        abort(401)
    else:
        abort(401)

@app.route('/logout', methods=['POST'])
def logout():
    param = request.get_json()
    if dbFunctions.killSession(param['session']):
        return 'OK'
from app import googleFit


@app.route('/predict/<string:id>')
def predict(id):
    prediction_list = { '54-501-042-01' : [0.9, 0.8, .8, 0, 0],
		    '54-501-044-010' : [0.7, 0, 0.9, 0, 0],
		    '54-501-007-01' :[0.9, 0, 0, 0, 0]				
                  }
    categories = ['Артериальная гипертензия', 
                  'ОНМК', 
                  'Стенокардия, ИБС, инфаркт миокарда',
                  'Сердечная недостаточность',
                  'Прочие заболевания сердца']

    N = len(categories)
    predictions = prediction_list[id]
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=10)

    predictions += predictions[:1]
    predictions

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.50,0.75], ["25%","50%","75%"], color="grey", size=10)
    plt.ylim(0.01)

    # Plot data
    ax.plot(angles, predictions, linewidth=2, linestyle='solid')

    # Fill area
    ax.fill(angles, predictions, 'b', alpha=0.1)
    #plt.show()
    #return fig_to_html(fig)
    x = np.arange(1, 8)
    y = np.random.randint(1, 20, size = 7)

    fig, ax = plt.subplots()

    ax.bar(x, y)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(3)    #  ширина Figure
    fig.set_figheight(2)    #  высота Figure
    return fig_to_html(fig)
