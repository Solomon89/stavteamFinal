import psycopg2
import uuid

deleteInterval = 3600
SERVER = '176.15.105.107'
DATABASE = 'stavteamdb'
UID = 'stavteamdb'
PWD = '111111'


def killExpiredSessions(interval):
    sql = '''delete FROM public.sessions WHERE extract(epoch  from (now()::timestamp-logintime))>''' + str(interval)
    execSQL(sql, True, False)


def checkSession(uid):
    killExpiredSessions(deleteInterval)
    sql = "select sessions.* FROM public.sessions where sessions.session='" + uid + "'"
    rows = execSQL(sql, None, True)
    return len(rows) > 0


def makeSession(userId):
    uid = str(uuid.uuid4())
    sql = '''INSERT INTO public.sessions(session, userid, logintime)
     VALUES
           (\'''' + uid + '''\',
            ''' + str(userId) + ''',NOW()::timestamp)'''
    param = [uid, userId]
    execSQL(sql, param, False)
    return uid


def killSession(uid):
    sql = "delete FROM public.sessions where sessions.session='" + uid + "'"
    execSQL(sql, True, False)
    return True


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


def checkToNull(param):
    if str(param) == '':
        s = ' NULL,'
    elif param is None:
        s = ' NULL,'
    else:
        s = " '" + param + "',"
    return s


def getRoofTypes():
    sql = 'SELECT id, "name" FROM public.roof_types;'
    rows = execSQL(sql, None, True)
    return rows


def getFuelTypes():
    sql = 'SELECT id, "name" FROM public.fuel_types;'
    rows = execSQL(sql, None, True)
    return rows

def getHeatTypes():
    sql = 'SELECT id, "name" FROM public.heat_sources;'
    rows = execSQL(sql, None, True)
    return rows

def getWaterSources():
    sql = 'SELECT id, "name" FROM public.water_sources;'
    rows = execSQL(sql, None, True)
    return rows

def getWaterTime():
    sql = 'SELECT id, "name" FROM public.water_times;'
    rows = execSQL(sql, None, True)
    return rows

def getProperties():
    sql = 'SELECT id, "name" FROM public.properties_types;'
    rows = execSQL(sql, None, True)
    return rows

def getUnits():
    sql = 'SELECT id, "name" FROM public.square_units;'
    rows = execSQL(sql, None, True)
    return rows

def getCoockingPlaces():
    sql = 'SELECT id, "name" FROM public.coocking_places;'
    rows = execSQL(sql, None, True)
    return rows

def getVentilations():
    sql = 'SELECT id, "name" FROM public.ventilations;'
    rows = execSQL(sql, None, True)
    return rows

def getAnswers():
    sql = 'SELECT id, "name" FROM public.answers;'
    rows = execSQL(sql, None, True)
    return rows

def getAssets():
    sql = 'SELECT id, "name" FROM public.assets;'
    rows = execSQL(sql, None, True)
    return rows

def getIncomingParts():
    sql = 'SELECT id, "name" FROM public.income_parts;'
    rows = execSQL(sql, None, True)
    return rows

def getIncomeLevels():
    sql = 'SELECT id, "name" FROM public.income_levels;'
    rows = execSQL(sql, None, True)
    return rows

def getHousingTypes():
    sql = 'SELECT id, "name" FROM public.housing_types;'
    rows = execSQL(sql, None, True)
    return rows