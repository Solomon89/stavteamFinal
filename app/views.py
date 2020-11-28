from stavteam import app
from flask import render_template
from flask import jsonify, request
from app import dbFunctions
from flask import abort

@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html", user="Stavteam")

@app.route('/login', methods=['POST'])
def login():
    param = request.get_json()
    sql = '''SELECT public.users.*, public.roles.name  FROM public.users 
             left outer join public.roles on  public.users.roleid= public.roles.id 
             where users.login='%s' ''' % param['userName']
    rows = dbFunctions.execSQL(sql, None, True)
    if len(rows) > 0:
        for row in rows:
            if row[4].strip() == param['userPass']:
                uid = dbFunctions.makeSession(row[0])
                userInfo = {'FAM': row[1], 'IM': row[2], 'OT': row[3], 'ROLE':row[7],  'SESSION': uid}
                return jsonify(userInfo)
        abort(401)
    else:
        abort(401)

from app import googleFit