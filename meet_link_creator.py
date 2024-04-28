import requests
import json
import datetime
import hmac
import hashlib
import base64

mail = 'damir.riyatov@gmail.com'# will be creator mail
Client_secret = 'CfI2vDSgbiIo8hpELrOuN1O1CQfPgP0s'
Client_ID = 'ghwuvh95Rd2tLtfzA1s_0w'

auth = b"ghwuvh95Rd2tLtfzA1s_0w:CfI2vDSgbiIo8hpELrOuN1O1CQfPgP0s" # Client_ID + ':' + Client_secret


def generateToken(mail: str):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.urlsafe_b64encode(auth)}"

    }

    body = {
        "grant_type": "account_credentials",
        "account_id": f"{mail}"
    }

    r = requests.post("https://zoom.us/oauth/token", headers=headers, data=body)

    return_data = r.json()
    print(return_data)
    access_token = return_data["access_token"]
    return access_token


def createMeeting(creator, start_time):
    headers = {
        'authorization': f'Bearer {generateToken(mail)}',
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

    r = requests.post(
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