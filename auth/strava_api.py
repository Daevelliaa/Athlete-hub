import requests

def get_strava_activities(access_token, after_timestamp=None, before_timestamp=None, per_page=200):
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {
        "per_page": per_page,
        "page": 1,
        "after": after_timestamp,
        "before": before_timestamp
    }

    activities = []

    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if not data:
            break

        activities.extend(data)
        params["page"] += 1

    return activities
