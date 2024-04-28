from pyzoom import *
import datetime
import json
import pytz
from flask import Flask, abort, request
from uuid import uuid4
import requests
import requests.auth
import urllib
"""
CLIENT_ID = "ghwuvh95Rd2tLtfzA1s_0w"  # Fill this in with your client ID
CLIENT_SECRET = "CfI2vDSgbiIo8hpELrOuN1O1CQfPgP0sT"  # Fill this in with your client secret
REDIRECT_URI = "http://localhost:65010/integrations/zoom"

app = Flask(__name__)


@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with Zoom</a>'
    return text % make_authorization_url()


def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks

    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "redirect_uri": REDIRECT_URI}
    url = "https://zoom.us/oauth/authorize?" + urllib.parse.urlencode(params)
    return url


@app.route('/zoom_callback')
def zoom_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error

    code = request.args.get('code')
    access_token = get_token(code)
    # Note: In most cases, you'll want to store the access token, in, say,
    # a session for use in other parts of your web app.
    return "Your user info is: %s" % get_username(access_token)


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}

    response = requests.post("https://zoom.us/oauth/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    print(token_json)
    return token_json["access_token"]


def get_username(access_token):
    headers = {"Authorization": "bearer " + access_token}
    response = requests.get("https://api.zoom.us/v2/users/damir.riyatov@gmail.com", headers=headers)
    me_json = response.json()
    return me_json


if __name__ == '__main__':
    app.run(debug=True, port=65010)

now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))

"""
CLIENT_ID = 'ghwuvh95Rd2tLtfzA1s_0w'
CLIENT_SECRET = 'CfI2vDSgbiIo8hpELrOuN1O1CQfPgP0s'

tokens = oauth_wizard(CLIENT_ID, CLIENT_SECRET)

ZOOM_ACCESS_TOKEN = tokens['access_token']

client = ZoomClient('ZOOM_ACCCESS_TOKEN', base_url="https://api.zoom.us/v2")

creator = "Damir"
start_time = datetime.datetime(2024, 4, 30, 10, 0)

def createMeeting(creator, start_time):
    headers = {
        'authorization': f"{tokens}",
        'content-type': 'application/json'
    }

    meeting_details = {
        "topic": f"Meeting created by {creator}",
        "type": 2,
        "start_time": f"{start_time.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "duration": "60",
        "timezone": "Europe/Moscow",
        "agenda": "",
        "recurrence": {"type": 1, "repeat_interval": 1},
        "settings": {
            "host_video": "true",
            "participant_video": "true",
            "join_before_host": "true",
            "mute_upon_entry": "False",
            "watermark": "false",
            "audio": "voip",
            "auto_recording": "cloud"
        }
    }

    r = requests.get(
        'https://api.zoom.us/v2/users/me/meetings',
        headers=headers,
        data=json.dumps(meeting_details)
    )

    if r.status_code == 201:
        response_data = r.json()
        join_url = response_data.get("join_url")
        password = response_data.get("password")
        return join_url, password
    else:
        print("Error creating Zoom meeting:", r.text)
        return None, None

createMeeting(creator, start_time)
