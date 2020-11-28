from datetime import datetime
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow, AccessTokenCredentials 
import httplib2
import matplotlib.pyplot as plt



CLIENT_ID = '488160995737-gufpaiscivjd6l3r3ofk9p5833g9gn38.apps.googleusercontent.com'
CLIENT_SECRET = 'ipNz9k7Qv0LIO04wPvEtsz_x'
OAUTH_SCOPE = ['https://www.googleapis.com/auth/fitness.heart_rate.read',
               'https://www.googleapis.com/auth/fitness.activity.read',
               'https://www.googleapis.com/auth/fitness.sleep.read']
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
DATA_SOURCE = "derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm"
DATA_SET = "1551700038292387000-1751700038292387000"


def nanoseconds(nanotime):
    """
    Convert epoch time with nanoseconds to human-readable.
    """
    dt = datetime.fromtimestamp(nanotime // 1000000000)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


#flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
#authorize_url = flow.step1_get_authorize_url()
#print('Go to the following link in your browser:')
#print(authorize_url)
#code = input('Enter verification code: ').strip()
#code='4/1AY0e-g41BqSTTB0lfWC4nN84hwvsjJO0t2StM4oiduowXCyNTRD_eVfIY2k'
#credentials = flow.step2_exchange(code)
credentials = AccessTokenCredentials('ya29.a0AfH6SMBpA9KNzKCv4QWXZA1nWINImf2DFaEpGT_nUgHbCjK4TPWkj-DDhXZjYpkpzoD_XEp6wXApEEBV_Yq7LVqrNqkyyVCDE6kyrmVArtM1iKLt_dz30pLbTzIjYf8qoSwH0uiUnLnKtwOpADnfl78hFAQWRbmk6lJpkPE2epM','my-user-agent/1.0')

http = httplib2.Http()
http = credentials.authorize(http)

fitness_service = build('fitness', 'v1', http=http)

#########################         Пульс
data = fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=DATA_SOURCE,
                                                            datasetId=DATA_SET).execute()

endData = {}
i = 0
for hr in data['point']:
    dt = datetime.fromtimestamp(int(hr['startTimeNanos']) // 1000000000)
    endData[str(i)] = {'startTime': dt, 'value': hr['value'][0]['fpVal']}
    i += 1
pulseData = endData
########################          Шаги
data = fitness_service.users().dataSources().datasets().get(userId='me',
                                                            dataSourceId='derived:com.google.step_count.delta:com.google.android.gms:estimated_steps',
                                                            datasetId=DATA_SET).execute()

endData = {}
i = 0
for hr in data['point']:
    dt1 = datetime.fromtimestamp(int(hr['startTimeNanos']) // 1000000000)
    dt2 = datetime.fromtimestamp(int(hr['endTimeNanos']) // 1000000000)
    endData[str(i)] = {'startTime': dt1, 'endTime': dt2, 'value': hr['value'][0]['intVal']}
    i += 1
stepData = endData
########################          Активность
data = fitness_service.users().dataSources().datasets().get(userId='me',
                                                            dataSourceId='derived:com.google.activity.segment:com.google.android.gms:merge_activity_segments',
                                                            datasetId=DATA_SET).execute()
endData = {}
i = 0
for hr in data['point']:
    dt1 = datetime.fromtimestamp(int(hr['startTimeNanos']) // 1000000000)
    dt2 = datetime.fromtimestamp(int(hr['endTimeNanos']) // 1000000000)
    endData[str(i)] = {'startTime': dt1, 'endTime': dt2, 'activityType': hr['value'][0]['intVal']}
    i += 1
activityData = endData

########################          Сон
data = fitness_service.users().dataSources().datasets().get(userId='me',
                                                            dataSourceId='derived:com.google.sleep.segment:com.google.android.gms:sleep_from_activity<-raw:com.google.activity.segment:com.xiaomi.hm.health:',
                                                            datasetId=DATA_SET).execute()
endData = {}
i = 0
for hr in data['point']:
    dt1 = datetime.fromtimestamp(int(hr['startTimeNanos']) // 1000000000)
    dt2 = datetime.fromtimestamp(int(hr['endTimeNanos']) // 1000000000)
    endData[str(i)] = {'startTime': dt1, 'endTime': dt2, 'activityType': hr['value'][0]['intVal']}
    i += 1
activityData = endData

