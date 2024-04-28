import requests
import json
import datetime
import hmac
import hashlib
import base64
import Access_token_generator
from flask import Flask, abort, request
from uuid import uuid4
import requests
import requests.auth
import urllib
import meet_link_creator

mail = 'damir.riyatov@gmail.com'# will be creator mail
Client_secret = 'CfI2vDSgbiIo8hpELrOuN1O1CQfPgP0s'
Client_ID = 'ghwuvh95Rd2tLtfzA1s_0w'

auth = b"ghwuvh95Rd2tLtfzA1s_0w:CfI2vDSgbiIo8hpELrOuN1O1CQfPgP0s" # Client_ID + ':' + Client_secret

def createMeeting(creator, start_time):
    headers = {
        'authorization': f'Bearer eyJzdiI6IjAwMDAwMSIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6ImUzY2E4NTM3LWQ5ZjYtNDZkMy1iODEzLTE3NTBjY2NhY2RmOSJ9.eyJ2ZXIiOjksImF1aWQiOiI1MDk1YTNlMWY3M2I4YzMyZDczOGQzMjdhZjNhMjBkMyIsImNvZGUiOiJCZVAwODNwenliNzNHRmZXY2hzVDVHendxcnZBbk5MTFEiLCJpc3MiOiJ6bTpjaWQ6Z2h3dXZoOTVSZDJ0THRmekExc18wdyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJTOWhyczVGeVQ2aTljVVlsSVl1NUhRIiwibmJmIjoxNzE0MjgxNjEyLCJleHAiOjE3MTQyODUyMTIsImlhdCI6MTcxNDI4MTYxMiwiYWlkIjoib0dkeGJLdzFSb2FaM3ZEckphMi1YdyJ9.357GS5xJrPa7aGbEHxERjmfS2yAIOao2WrE_pVRdhwJjlqIu1aaCiZum-t6GU-sP5EGpn--T0CQWTOeUp3lCdw', 'token_type': 'bearer', 'refresh_token': 'eyJzdiI6IjAwMDAwMSIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6IjY5NzFiMGEwLTA5ODgtNGI4NS1hMDZmLTJkZjdmM2FlNjg2NSJ9.eyJ2ZXIiOjksImF1aWQiOiI1MDk1YTNlMWY3M2I4YzMyZDczOGQzMjdhZjNhMjBkMyIsImNvZGUiOiJCZVAwODNwenliNzNHRmZXY2hzVDVHendxcnZBbk5MTFEiLCJpc3MiOiJ6bTpjaWQ6Z2h3dXZoOTVSZDJ0THRmekExc18wdyIsImdubyI6MCwidHlwZSI6MSwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJTOWhyczVGeVQ2aTljVVlsSVl1NUhRIiwibmJmIjoxNzE0MjgxNjEyLCJleHAiOjE3MjIwNTc2MTIsImlhdCI6MTcxNDI4MTYxMiwiYWlkIjoib0dkeGJLdzFSb2FaM3ZEckphMi1YdyJ9.aipowhs6AsKlgShwxMTG0QIybhFTh2Xv8MnoPqQuSTUFMylavU8WQKW3wOkkg8mz3Kd5reQ2k9YRYHmhqq-3Gw', 'expires_in': str(3599), 'scope': 'meeting:write:meeting:admin',
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


# Example usage
if __name__ == "__main__":
    creator = "Damir"
    start_time = datetime.datetime(2024, 4, 30, 10, 0)  # Example: April 30, 2024, 10:00 AM

    join_url, password = createMeeting(creator, start_time)
    print(join_url, password)
    if join_url:
        print("Meeting created successfully!")
        print("Join URL:", join_url)
        print("Meeting Password:", password)
    else:
        print("Failed to create meeting.")