import psycopg2
import uuid
from app import graph

deleteInterval = 3600
SERVER = '176.118.165.45'
DATABASE = 'stavteamdb'
UID = 'stavuser'
PWD = 'password'


def killExpiredSessions(interval):
    sql = '''delete FROM public.sessions WHERE extract(epoch  from (now()::timestamp-"loginTime"))>''' + str(interval)
    execSQL(sql, True, False)


def checkSession(uid):
    killExpiredSessions(deleteInterval)
    sql = "select sessions.* FROM public.sessions where sessions.session='" + uid + "'"
    rows = execSQL(sql, None, True)
    return len(rows) > 0


def makeSession(userId):
    uid = str(uuid.uuid4())
    sql = '''INSERT INTO public.sessions(session, "userID", "loginTime")
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


def getlineStatus(lineId):
    sql = ('SELECT linestatus.*,statuses."Name" FROM public.linestatus ' +
           ' left outer join public.statuses on linestatus.status_id = statuses.id ' +
           ' where linestatus.line_id=' + str(lineId) +
           ' order by linestatus.id desc')
    lineStatuses = execSQL(sql, True, True)
    lineStatusesJSON = {}
    for lineStatus in lineStatuses:
        lineStatusesJSON[lineStatus[0]] = {'dateOfEvent': lineStatus[1],
                                           'fileName': lineStatus[2],
                                           'statusId': lineStatus[3],
                                           'lineId': lineStatus[4],
                                           'statusName': lineStatus[5]}


def getLinks():
    sql = "SELECT links.* FROM public.links"
    links = execSQL(sql, True, True)
    linksJSON = {}
    for link in links:
        linksJSON[link[0]] = {'idRecorderIn': link[1],
                              'idRecorderOut': link[2]}
    return linksJSON


def getRecorders(needFullInfo=False):
    sql = "SELECT recorder.* FROM public.recorder"
    recorders = execSQL(sql, True, True)
    recordersJSON = {}
    for recorder in recorders:
        if needFullInfo:
            recordersJSON[recorder[0]] = {'stationId': recorder[1],
                                          'name': recorder[2],
                                          'direction': recorder[3],
                                          'folder': recorder[4]}
        else:
            recordersJSON[recorder[0]] = {'stationId': recorder[1],
                                          'name': recorder[2],
                                          'direction': recorder[3]}
    return recordersJSON


def getStations(needFullInfo=False):
    sql = "SELECT station.* FROM public.station"
    stations = execSQL(sql, True, True)
    stationsJSON = {}
    for station in stations:
        if needFullInfo:
            stationsJSON[station[0]] = {'name': station[1],
                                        'lon': station[2],
                                        'lat': station[3],
                                        'ftpAdress': station[4],
                                        'ftpPassword': station[5],
                                        'ftpUser': station[6]}
        else:
            stationsJSON[station[0]] = {'name': station[1],
                                        'lon': station[2],
                                        'lat': station[3]}
    return stationsJSON


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


def getEventFilePath(eventId):
    sql = "SELECT linestatus.filename FROM public.linestatus where linestatus.id=" + str(eventId)
    recorders = execSQL(sql, True, True)
    return recorders[0][0]


def newEvent(station, filename):
    eventDate, analogLineCount, digitalLineCount = graph.getEventInfo(filename)
    sql = ('INSERT INTO public.linestatus(dateofevent, filename, line_id, "analogLineCount", "digitalLineCount") ' +
           " VALUES ('" + str(eventDate) + "', '" + filename + "', " + station +
           "," + str(analogLineCount) + "," + str(digitalLineCount) + ") ")
    execSQL(sql, True, False)


def updateEvent(id, params):
    sql = ('UPDATE public.linestatus SET status_id=' + str(params['Type']) +
           ", timeof='" + params['TimeOf'] + "', apv='" + params['APV'] +
           "', distancetokz='" + params['distanceToKZ'] + "' " +
           'WHERE id=' + str(id))
    execSQL(sql, True, False)


def getStatuses():
    sql = "SELECT * FROM public.statuses"
    rows = execSQL(sql, True, True)
    statuses = {}
    for row in rows:
        statuses[row[0]] = {'name': row[1]}
    return statuses


def getUnProcssedEvents():
    sql = "SELECT linestatus.* FROM public.linestatus where linestatus.status_id is NULL"
    lineStatuses = execSQL(sql, True, True)
    lineStatusesJSON = {}
    for lineStatus in lineStatuses:
        lineStatusesJSON[lineStatus[0]] = {'dateOfEvent': lineStatus[1],
                                           'fileName': lineStatus[2],
                                           'statusId': lineStatus[3],
                                           'lineId': lineStatus[4],
                                           'timeOf': lineStatus[5],
                                           'apv': lineStatus[6],
                                           'distanceToKz': lineStatus[7],
                                           'analogLineCount': lineStatus[8],
                                           'digitalLineCount': lineStatus[9]}
    return lineStatusesJSON
