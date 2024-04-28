import requests
import json
import datetime
import hmac
import hashlib
import base64

# Найди правильные API_KEY и API_SEC и я тебя не убью
API_KEY = 'jV5p1MXGTtqcvzDPEu4WA'
API_SEC = 'TPUt9gOJXnaPtkSGeLZDz6wTw4NA79kC'


def generateToken():
    payload = {
        'iss': API_KEY,
        'exp': int(datetime.datetime.utcnow().timestamp()) + 10900  # Token expires in 1 hour
    }

    header = {
        'alg': 'HS256',
        'typ': 'JWT'
    }

    header_encoded = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().strip('=')
    payload_encoded = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().strip('=')

    data = header_encoded + '.' + payload_encoded
    signature = hmac.new(API_SEC.encode(), msg=data.encode(), digestmod=hashlib.sha256).digest()
    signature_encoded = base64.urlsafe_b64encode(signature).decode().strip('=')

    return data + '.' + signature_encoded


def createMeeting(creator, start_time):
    headers = {
        'authorization': f'Bearer {generateToken()}',
        'content-type': 'application/json'
    }

    meeting_details = {
        "topic": f"Meeting created by {creator}",
        "type": 2,
        "start_time": start_time.strftime('%Y-%m-%dT%H:%M:%S'),
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