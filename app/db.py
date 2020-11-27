import psycopg2
import uuid


deleteInterval = 3600
SERVER = '176.15.105.107'
DATABASE = 'stavteamdb'
UID = 'stavteamdb'
PWD = '111111'


def GetAuth():
    sql = 'SELECT * FROM authgoogle LIMIT 10'
    value = execSQL(sql, True, False)
    return value

def SaveAuth(code):
    sql = "insert into authgoogle(name) values '"+code+"'"
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