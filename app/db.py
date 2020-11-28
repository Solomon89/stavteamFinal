import psycopg2
import uuid
from app.models import GoogleUser

deleteInterval = 3600
SERVER = '176.15.105.107'
DATABASE = 'stavteamdb'
UID = 'stavteamdb'
PWD = '111111'


def GetAuth(unique_id):
    _return = ""
    sql = "SELECT * FROM usergoogle where unique_id = '" +unique_id+ "'"
    value = execSQL(sql, True, True)
    for user in value:
        _return += str(user)
    return value[0]

def SaveAuth(GoogleUser):

    sql = "insert into usergoogle (name,email,profile_pic,unique_id) values (" +GoogleUser.inLineToSave() + ")"
    execSQL(sql, True, False)



def execSQL(sql, param, needFeatch):
    cnxn = psycopg2.connect(dbname=DATABASE, user=UID,
                            password=PWD, host=SERVER)
    cursor = cnxn.cursor()
    cursor.execute(sql)
    if needFeatch:
        rows = cursor.fetchall()
        cnxn.close()
        return rows
    else:
        try:
            ids = cursor.fetchone()[0]
        except:
            ids = None
        cnxn.commit()
        cnxn.close()
        return ids