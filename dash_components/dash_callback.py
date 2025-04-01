from dash.dependencies import Input, Output
from datetime import datetime
import plotly.graph_objs as go
import pandas as pd
import time
import flask
from auth.strava_api import get_strava_activities
from dash_components.first_graphique import create_graphique
from dash_components.donut_chart import create_donut_graphique
from dash_components.first_scatter import scatter_distance_power
from dash_components.scatter_PR import scatter_pr
from dash import no_update, html

def register_callbacks(dash_app):

    def loading_fig():
        fig = go.Figure()
        fig.add_annotation(text="Loading...", x=0.5, y=0.5, showarrow=False, font=dict(size=20))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_visible=False,
            yaxis_visible=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        return fig

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
        #print("Athlete =", athlete)
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
        Output('Bar_chart', 'style'),
        Output('Donut_first_chart','figure'),
        Output('Donut_first_chart','style'),
        Output('kudos-count-text','children'),
        Output('comment-count-text','children'),
        Output('scatter_power_distance', 'figure'),
        Output('scatter_power_distance', 'style'),
        Output('Scatter_PR', 'figure'),
        Output('Scatter_PR', 'style'),
        Input('activities_2024','data')
    )
    def update_bar_chart(activities):
        if not activities:
            fig=loading_fig()
            style = {'width': '100%', 'height': '100%', 'display': 'block'}
            return fig, style, fig, style,"0","0",fig,style,fig,style

        
        #Convertir la liste en DataFrame
        df=pd.DataFrame(activities)

        #On garde les colonnes utiles 
        if 'start_date' not in df:
            fig = loading_fig()
            style = {'width': '100%', 'height': '100%', 'display': 'block'}
            return fig, style, fig, style,"0","0",fig,style,fig,style

        bar_fig = create_graphique(df)
        donut_fig = create_donut_graphique(df)
        scatter_power_distance=scatter_distance_power(df)
        scatter_pr_month=scatter_pr(df)
        style = {'width': '100%', 'height': '100%', 'visibility': 'visible'}
        total_kudos=df['kudos_count'].sum() if 'kudos_count'in df else 0
        total_comments = df['comment_count'].sum() if 'comment_count' in df else 0

        return bar_fig, style, donut_fig, style, str(total_kudos),str(total_comments), scatter_power_distance, style, scatter_pr_month, style
         
