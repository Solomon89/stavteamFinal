from flask import Flask
import os


from oauthlib.oauth2 import WebApplicationClient
import requests

# Configuration

import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask(__name__)

app.secret_key = "4vxLyDnY7ylkd1F6Q8-5JvaD"


client = WebApplicationClient("473752170137-lu6o3d86puh7i6f8v5a1h93apv1evbmt.apps.googleusercontent.com")

from app import views

if __name__ == "__main__":
    app.run(port=4345)

