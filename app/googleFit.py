from stavteam import app,client
from flask import render_template
from flask import Flask, redirect, request, url_for
from app import db
import requests
import json

@app.route('/auth')
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def get_google_provider_cfg():
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()

@app.route('/auth/callback')
def callback():
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
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    #db.SaveAuth(str(userinfo_response))
    return userinfo_response.json()["picture"]