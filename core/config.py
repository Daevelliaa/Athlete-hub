import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID=os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET=os.getenv("STRAVA_CLIENT_SECRET")
SECRET_KEY_FLASK=os.getenv("SECRET_KEY")