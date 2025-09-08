import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "size": 50.0,
    "nb_rooms": 3,
    "garden": True
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Prediction :", response.json())
else:
    print("Erreur :", response.status_code, response.text)
