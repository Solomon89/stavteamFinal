from stavteam import app,client
from flask import render_template
from flask import Flask, redirect, request, url_for, session
from app import db
import requests
import json
from app.models import GoogleUser

@app.route('/auth/<int:userId>')
def auth2(userId):
    user = db.GetGoogleAuth(userId)
    if(user == None):
        session['id'] = str(id)
        return redirect(url_for("auth"))

    return str(user)
@app.route('/auth')
def auth():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    
    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile",'https://www.googleapis.com/auth/fitness.heart_rate.read','https://www.googleapis.com/auth/fitness.activity.read',
               'https://www.googleapis.com/auth/fitness.sleep.read'],
    )
    print(request_uri)
    return redirect(request_uri)

def get_google_provider_cfg():
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()

@app.route('/auth/callback')
def callback():
    id =  session['id'] 
    redirect("https://www.googleapis.com/auth/fitness.activity.read")
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=("473752170137-lu6o3d86puh7i6f8v5a1h93apv1evbmt.apps.googleusercontent.com", "4vxLyDnY7ylkd1F6Q8-5JvaD"),
    )
    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    print(token_response.json())
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        access_token = token_response.json()["access_token"]
        User = GoogleUser.GoogleUser(unique_id,users_email,picture,users_name,id,access_token)
        db.SaveAuth(User)
    else:
        return "User email not available or not verified by Google.", 400

    
    return '<p>'+User.users_email+'</p><img src="'+User.picture+'" alt="альтернативный текст">'

@app.route('/myauth/<string:uniq_id>')
def myauth(uniq_id):
    _return = ""
    user = db.GetAuth(uniq_id)
    for items in user:
        _return += str(items)
    return _return


