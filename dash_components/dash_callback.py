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
from dash_components.biggest_activity import biggest_activity_map
from dash_components.activity_count_bar import activity_count_bar
from dash_components.distance_range_donut import distance_range_donut
from dash_components.scatter_temp_speed import scatter_temp_speed
from dash_components.radar_chart import radar_hr_zones
from dash_components.scatter_distance_elevation import scatter_distance_elevation
from dash_components.heatmap import create_heatmap_matrix_from_df, create_heatmap_figure_from_matrix
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
            return f"Welcome {prenom} {nom} in your Dashboard !"
        return "Bienvenue dans ton Dashboard"
    

    @dash_app.callback(
        Output('yearly_activities_store', 'data'),
        Input('athlete_store', 'data'),            # ⬅️ déclenche au chargement utilisateur
        Input('date-range-picker','start_date'),
        Input('date-range-picker','end_date')            # ⬅️ on lit la plage séléctionnée
    )
    def load_activities_for_period(athlete, start_date, end_date):
        if not athlete or not start_date or not end_date:
            return []

        token = flask.session.get('access_token')
        after = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
        before = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())
    
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
        Output('map', 'figure'),
        Output('map', 'style'),
        Output('map-title', 'children'),
        Output('map-distance', 'children'),
        Output('map-elevation', 'children'),
        Output('map-speed', 'children'),
        Output('activity-count', 'figure'),
        Output('activity-count', 'style'),
        Output('range-donut', 'figure'),
        Output('range-donut', 'style'),
        Output('scatter-temp', 'figure'),
        Output('scatter-temp', 'style'),
        Output('radar', 'figure'),
        Output('radar', 'style'),
        Output('scatter-elevation', 'figure'),
        Output('scatter-elevation', 'style'),
        Input('yearly_activities_store', 'data')
    )

    def update_graphs(activities):
        if not activities:
            fig = loading_fig()
            style = {'width': '100%', 'height': '100%', 'display': 'block'}
            return fig, style, fig, style, "0", "0", fig, style, fig, style, fig, style, fig, style,"0","0","0","0","0","0",fig,style,fig,style,fig,style,"","","","",fig,style,fig,style,fig,style,fig,style,fig,style

        df = pd.DataFrame(activities)
        if 'start_date' not in df:
            fig = loading_fig()
            style = {'width': '100%', 'height': '100%', 'display': 'block'}
            return fig, style, fig, style, "0", "0", fig, style, fig, style, fig, style, fig, style,"0","0","0","0","0","0",fig,style,fig,style,fig,style,"","","","","",fig,style,fig,style,fig,style,fig,style,fig,style

        # Génération des graphes
        bar_fig = create_graphique(df)
        donut_fig = create_donut_graphique(df)
        scatter_power_distance = scatter_distance_power(df)
        scatter_pr_month = scatter_pr(df)
        scatter_start = scatter_start_time(df)
        donut_total_hours = total_hours_donut(df)
        hr_speed=scatter_hr_speed(df)
        elevation=bar_elevation(df)
        map=biggest_activity_map(df)
        activity_count=activity_count_bar(df)
        range_donut=distance_range_donut(df)
        scatter_temp=scatter_temp_speed(df)
        radar_chart=radar_hr_zones(df)
        scatter_elevation=scatter_distance_elevation(df)

        style = {'width': '100%', 'height': '100%', 'visibility': 'visible'}
        total_kudos = df['kudos_count'].sum() if 'kudos_count' in df else 0
        total_comments = df['comment_count'].sum() if 'comment_count' in df else 0
        top_speed = round(df["max_speed"].max() * 3.6, 1)
        max_watts=df["max_watts"].max()
        high_heart=df["max_heartrate"].max()
        most_elevation=df["total_elevation_gain"].max()
        most_pr=df["pr_count"].sum()
        kilojoules=df["kilojoules"].max()
        biggest = df.loc[df['distance'].idxmax()]
        name = biggest.get('name', 'Sortie inconnue')
        distance_km = round(biggest['distance'] / 1000, 1)
        elevation_2 = round(biggest.get('total_elevation_gain', 0))
        moving_time_hours = biggest['moving_time'] / 3600
        speed_kmh = round(distance_km / moving_time_hours, 1) if moving_time_hours > 0 else 0

        distance_text = [
            "Distance", html.Br(), f"{distance_km}", html.Br(), "km"
        ]

        elevation_text = [
            "Elevation", html.Br(), f"{elevation_2}", html.Br(), "m"
        ]

        speed_text = [
            "Speed", html.Br(), f"{speed_kmh}", html.Br(), "km/h"
            ]



        return bar_fig, style, donut_fig, style, str(total_kudos), str(total_comments), scatter_power_distance, style, scatter_pr_month, style, scatter_start, style, donut_total_hours, style,top_speed,max_watts,high_heart,most_elevation,most_pr,kilojoules,hr_speed,style,elevation,style,map,style,name, distance_text, elevation_text, speed_text,activity_count,style,range_donut,style,scatter_temp,style,radar_chart,style,scatter_elevation,style
    

    @dash_app.callback(
        Output('year', 'data'),
        Input('year-selector', 'value'),
        Input('athlete_store', 'data')
    )
    def fetch_year_data(selected_year, athlete):
        if not selected_year or not athlete:
            return []
        
        token = flask.session.get('access_token')
        after = int(datetime(selected_year, 1, 1).timestamp())
        before = int(datetime(selected_year + 1, 1, 1).timestamp())
        activities = get_strava_activities(token, after, before)

        return activities


    @dash_app.callback(
        Output('heatmap-container', 'figure'),
        Output('heatmap-container','style'),
        Input('year', 'data'),
        Input('year-selector', 'value')
    )

    def update_heatmap(activities, year):
        if not activities or not year:
            return no_update

        df = pd.DataFrame(activities)
        if 'start_date' not in df or 'moving_time' not in df:
            return no_update

        matrix = create_heatmap_matrix_from_df(df, year)
        fig = create_heatmap_figure_from_matrix(matrix, year)
        style = {'width': '100%', 'visibility': 'visible'}

        return fig, style
        