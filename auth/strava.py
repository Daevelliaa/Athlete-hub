import requests
from core.config import CLIENT_ID, CLIENT_SECRET

def exchange_code_access_token(code):
    url="https://www.strava.com/oauth/token"
    data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type":"authorization_code"
    }

    response=requests.post(url, data=data)

    if response.status_code==200:
        return response.json()
    
    else:
        raise Exception(f"Erreur Strava : {response.text}")
