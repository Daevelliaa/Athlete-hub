from dash.dependencies import Input, Output, State
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
from dash_components.start_time_scatter import scatter_start_time
from dash_components.total_hours_donut import total_hours_donut
from dash_components.scatter_HR_speed import scatter_hr_speed
from dash_components.bar_elevation import bar_elevation
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
        Output('welcome-text', 'children'),
        Input('athlete_store', 'data'),        # ← ici tu dois recevoir un DICTIONNAIRE      
    )
    def update_welcome_message(athlete):
        #print("Athlete =", athlete)
        #print("Activities =", activities)

        if athlete:
            prenom = athlete.get('firstname', 'Athlète')
            nom = athlete.get('lastname', '')
            return f"Bienvenue {prenom} {nom} 👋"
        return "Bienvenue dans ton Dashboard"
    

    @dash_app.callback(
        Output('yearly_activities_store', 'data'),
        Input('athlete_store', 'data'),            # ⬅️ déclenche au chargement utilisateur
        Input('year-selector', 'value')            # ⬅️ on lit l’année par défaut
    )
    def load_activities_for_year(athlete, selected_year):
        if not athlete or not selected_year:
            return []

        token = flask.session.get('access_token')
        after = int(time.mktime(datetime(selected_year, 1, 1).timetuple()))
        before = int(time.mktime(datetime(selected_year + 1, 1, 1).timetuple()))
    
        activities = get_strava_activities(token, after, before)
        return activities



    @dash_app.callback(
        Output('Bar_chart', 'figure'),
        Output('Bar_chart', 'style'),
        Output('Donut_first_chart', 'figure'),
        Output('Donut_first_chart', 'style'),
        Output('kudos-count-text', 'children'),
        Output('comment-count-text', 'children'),
        Output('scatter_power_distance', 'figure'),
        Output('scatter_power_distance', 'style'),
        Output('Scatter_PR', 'figure'),
        Output('Scatter_PR', 'style'),
        Output('Scatter_start', 'figure'),
        Output('Scatter_start', 'style'),
        Output('donut_total_hours', 'figure'),
        Output('donut_total_hours', 'style'),
        Output('top_speed','children'),
        Output('max_watts','children'),
        Output('highest_heartrate','children'),
        Output('most_elevation','children'),
        Output('pr','children'),
        Output('athlete','children'),
        Output('scatter_hr_speed', 'figure'),
        Output('scatter_hr_speed', 'style'),
        Output('elevation', 'figure'),
        Output('elevation', 'style'),
        Input('yearly_activities_store', 'data')
    )

    def update_graphs(activities):
        if not activities:
            fig = loading_fig()
            style = {'width': '100%', 'height': '100%', 'display': 'block'}
            return fig, style, fig, style, "0", "0", fig, style, fig, style, fig, style, fig, style,"0","0","0","0","0","0",fig,style,fig,style

        df = pd.DataFrame(activities)
        if 'start_date' not in df:
            fig = loading_fig()
            style = {'width': '100%', 'height': '100%', 'display': 'block'}
            return fig, style, fig, style, "0", "0", fig, style, fig, style, fig, style, fig, style,"0","0","0","0","0","0",fig,style,fig,style

        # Génération des graphes
        bar_fig = create_graphique(df)
        donut_fig = create_donut_graphique(df)
        scatter_power_distance = scatter_distance_power(df)
        scatter_pr_month = scatter_pr(df)
        scatter_start = scatter_start_time(df)
        donut_total_hours = total_hours_donut(df)
        hr_speed=scatter_hr_speed(df)
        elevation=bar_elevation(df)

        style = {'width': '100%', 'height': '100%', 'visibility': 'visible'}
        total_kudos = df['kudos_count'].sum() if 'kudos_count' in df else 0
        total_comments = df['comment_count'].sum() if 'comment_count' in df else 0
        top_speed = round(df["max_speed"].max() * 3.6, 1)
        max_watts=df["max_watts"].max()
        high_heart=df["max_heartrate"].max()
        most_elevation=df["total_elevation_gain"].max()
        most_pr=df["pr_count"].sum()
        kilojoules=df["kilojoules"].max()

        return bar_fig, style, donut_fig, style, str(total_kudos), str(total_comments), scatter_power_distance, style, scatter_pr_month, style, scatter_start, style, donut_total_hours, style,top_speed,max_watts,high_heart,most_elevation,most_pr,kilojoules,hr_speed,style,elevation,style
