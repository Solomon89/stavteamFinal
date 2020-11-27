from datetime import datetime
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
import httplib2
import matplotlib.pyplot as plt

CLIENT_ID = '488160995737-gufpaiscivjd6l3r3ofk9p5833g9gn38.apps.googleusercontent.com'
CLIENT_SECRET = 'ipNz9k7Qv0LIO04wPvEtsz_x'
OAUTH_SCOPE='https://www.googleapis.com/auth/fitness.heart_rate.read'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
DATA_SOURCE = "derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm"
DATA_SET = "1551700038292387000-1751700038292387000"


def nanoseconds(nanotime):
    """
    Convert epoch time with nanoseconds to human-readable.
    """
    dt = datetime.fromtimestamp(nanotime // 1000000000)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print ('Go to the following link in your browser:')
print (authorize_url)
code = input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

http = httplib2.Http()
http = credentials.authorize(http)

fitness_service = build('fitness', 'v1', http=http)

data=fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=DATA_SOURCE, datasetId=DATA_SET).execute()

endData={}
for hr in data['point']:
    dt = datetime.fromtimestamp(int(hr['startTimeNanos']) // 1000000000)
    endData[str(dt)]=hr['value'][0]['fpVal']

days=list(endData.keys())
heartRates=list(endData.values())

plt.figure(figsize=(12, 7))

plt.plot(days[:200], heartRates[:200], 'o-r', alpha=0.7, label="first", lw=0.5, mec='b', mew=0.5, ms=1)
plt.show()
