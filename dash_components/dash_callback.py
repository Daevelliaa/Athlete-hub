from dash.dependencies import Input, Output
from datetime import datetime
import plotly.graph_objs as go
import pandas as pd
import time
import flask
from auth.strava_api import get_strava_activities
from dash_components.first_graphique import create_graphique

def register_callbacks(dash_app):

    @dash_app.callback(
        Output('athlete_store', 'data'),
        Input('welcome-text', 'id')
    )
    def store_athlete_data(_):
        return flask.session.get('athlete')


    @dash_app.callback(
    Output('activities_2024', 'data'),
    Input('athlete_store', 'data')  # On déclenche le chargement quand l'utilisateur est connecté
)
    def load_activities_2024(athlete):
        if not athlete:
            return []

        token = flask.session.get('access_token')

        # Timestamp début 2024 et fin 2024
        after = int(time.mktime(datetime(2024, 1, 1).timetuple()))
        before = int(time.mktime(datetime(2025, 1, 1).timetuple()))

        activities = get_strava_activities(token, after, before)
       
        return activities

    @dash_app.callback(
        Output('welcome-text', 'children'),
        Input('athlete_store', 'data'),        # ← ici tu dois recevoir un DICTIONNAIRE
        Input('activities_2024', 'data')       # ← ici tu reçois une LISTE
    )
    def update_welcome_message(athlete, activities):
        print("Athlete =", athlete)
        #print("Activities =", activities)

        if athlete:
            prenom = athlete.get('firstname', 'Athlète')
            nom = athlete.get('lastname', '')
            count = len(activities) if activities else 0
            return f"Bienvenue {prenom} {nom} 👋 — Tu as {count} activités en 2024 !"
        return "Bienvenue dans ton Dashboard"
    
    @dash_app.callback(
        #id du dcc.Graph Bar-chart
        Output('Bar_chart', 'figure'),
        Input('activities_2024','data')
    )
    def update_bar_chart(activities):
        if not activities:
            return go.Figure()
        
        #Convertir la liste en DataFrame
        df=pd.DataFrame(activities)

        #On garde les colonnes utiles 
        if 'start_date' not in df or 'distance' not in df:
            return go.Figure()
        
        # Appeler ta fonction personnalisée
        return create_graphique(df)
         
