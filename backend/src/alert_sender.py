import requests

def send_alert(video_path):
    url = "http://localhost:5000/api/alerts/upload"

    files = {"video": open(video_path, "rb")}
    data = {
        "driverId": "123",
        "message": "Drowsiness Detected"
    }

    try:
        res = requests.post(url, files=files, data=data)
        print("Uploaded:", res.text)
    except Exception as e:
        print("Error:", e)