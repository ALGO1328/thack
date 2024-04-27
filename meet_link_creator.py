import datetime
import pytz
import requests
import jwt
import json
import time  # Added time module import

# Enter your API key and your API secret
API_KEY = 'ffBmOzGDQpG6ReFkpyVALw'
API_SEC = 'UjaoYVT8St2PgaqveCnadQ'

# Correcting time format for JWT token expiration
def generateToken():
    expiration_time = int(time.time()) + 5000  # Current time + 5000 seconds
    payload = {'iss': API_KEY, 'exp': expiration_time}
    token = jwt.encode(payload, API_SEC, algorithm='HS256')
    return token.decode('utf-8')

# Define meeting details properly
def meetingdetails(creator: str, time: int):
    meetingdetails = {
        "topic": f"Встреча {creator}",
        "type": 2,
        "start_time": datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "duration": "45",
        "timezone": "Europe/Moscow",
        "agenda": "",
        "recurrence": {"type": 1, "repeat_interval": 1},
        "settings": {
            "host_video": "true",
            "participant_video": "true",
            "join_before_host": "true",
            "mute_upon_entry": "False",
            "watermark": "true",
            "audio": "voip",
            "auto_recording": "cloud"
        }
    }
    return meetingdetails

def createMeeting(creator, time):
    headers = {'authorization': 'Bearer ' + generateToken(), 'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers,
        data=json.dumps(meetingdetails(creator, time))
    )
    print("\nCreating zoom meeting...\n")
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
    return join_URL, meetingPassword



print(createMeeting("Damir", 	1714237200))
