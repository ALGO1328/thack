import datetime

import pytz

import requests

import jwt

import requests

import json

import meetings
from meetings import Meeting

import dateconv


# Enter your API key and your API secret
API_KEY = 'ffBmOzGDQpG6ReFkpyVALw'
API_SEC = 'Oi_STeQoQPu6d885cV4KCA'


def generateToken():
    token = jwt.encode(

        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},

        # Secret used to generate token signature
        API_SEC,

        # Specify the hashing alg
        algorithm='HS256'
    )
    return token.decode('utf-8')


# create json data for post requests
meetingdetails = {"topic": f"Встреча {Meeting.creator}",
                  "type": 2,
                  "start_time": f"2019-06-14T10: 21: 57{dateconv.from_unix(meetings.Meeting)}",
                  "duration": "45",
                  "timezone": "Europe/Moscow",
                  "agenda": "",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "true",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }


def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]

    return join_URL, meetingPassword

def create_link(time=int((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds())):
    print(time)
    pass

