import dash
from dash import html, dcc

from dash_components.first_graphique import create_graphique
from dash_components.donut_chart import create_donut_graphique
from dash_components.first_scatter import scatter_distance_power
from dash_components.scatter_PR import scatter_pr
from dash_components.my_heatmap import heatmap
from dash_components.start_time_scatter import scatter_start_time
from dash_components.total_hours_donut import total_hours_donut
from dash_components.scatter_HR_speed import scatter_hr_speed
from dash_components.bar_elevation import bar_elevation

def create_dash_app(flask_app):
    # Assurez-vous que Dash est correctement configuré avec Flask
    dash_app = dash.Dash(__name__,server=flask_app,routes_pathname_prefix='/dashboard/',)
    
    

    # Définir la mise en page de Dash
    dash_app.layout = html.Div(
        id='dash-container',  # Appliquer une classe CSS style.css stocké dans assets
        children=[
            # Titre de la page
            dcc.Store(id='athlete_store'),
            dcc.Store(id="activities_2024"),
            html.P(id='welcome-text', style={"text-align": "left"}),


            # Div principale qui contient les 4 boîtes
            html.Div(
                className="flex-container",  # Classe pour utiliser Flexbox
                children=[
                    html.Div(
                        className="box1",
                        children=[heatmap()]
                    ),

                    #Item/Box pour les total hours per month 
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('rocket.svg'), className="box-icon"),
                                    html.Div([
                                        html.P("Total Distance", className="box-title"),
                                        html.P("total distance per month", className="box-subtitle"),
                                    ])
                                ]
                            ),
                                dcc.Graph(
                                    id='Bar_chart',
                                    config={'displayModeBar': False, 'responsive': True},
                                    style={'width': '100%', 'height': '100%', 'visibility': 'hidden'}
                                ),
                            
                        ]
                    ),

                    #Item ou Box pour le nombre de jours de repos / jours actifs
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('bed.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Rest Days",className="box-title"),
                                        html.P("rest days vs. active days", className="box-subtitle"),
                                    ])
                                ]
                            ),
                                dcc.Graph(
                                    id='Donut_first_chart',
                                    config={'displayModeBar': False, 'responsive': True},
                                    style={'width': '100%', 'height': '100%', 'visibility': 'hidden'}
                                ),
                            
                        ]
                    ),
                ]
            ),

            # Div principale qui contient les 4 boîtes
            html.Div(
                className="flex-container",  # Classe pour utiliser Flexbox
                children=[

                    #Item ou Box pour les kudos et commentaires 
                    html.Div(
                        className="box",
                        children=[html.Div(
                            className="box-header",
                            children=[
                                html.Img(src=dash.get_asset_url('thumbs-up.svg'),className="box-icon"),
                                html.Div(
                                    children=[
                                        html.P("Socials", className="box-title"),
                                        html.P("total kudos and comments received", className="box-subtitle")
                                    ]
                                )
                                
                            ]

                        ),
                        html.Div(
                            className="social-content",
                            children=[
                                html.Div(
                                    className="social-content-item",
                                    children=[
                                        html.P("Kudos Count", className="kudos-count"),
                                        html.P("", id='kudos-count-text', className="kudos"),
                                        html.P("kudos", className="kudos-text")],
                                ),
                                html.Div(
                                    className="social-content-item",
                                    children=[
                                        html.P("Comment Count", className="kudos-count"),
                                        html.P("",id='comment-count-text', className="kudos"),
                                        html.P("comments",className="kudos-text")],
                                ),
                                

                            ]
                        )
                                  ]
                    ),

                    #Le graph scatter avec power vs distance et la régréssion linéaire très stylé
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('zap.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Distance vs. Power ", className="box-title"),
                                        html.P("power output per distance", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='scatter_power_distance',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'}
                            ),
                        ]
                    ),

                    # Ici un scatter avec les Personnal Records tous les mois

                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('medal.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("PRs", className="box-title"),
                                        html.P("prs achieved per month", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='Scatter_PR',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'}
                            ),
                            ]
                    ),

                    #Ici un scatter avec l'heure de départ des différentes activités dans la journée

                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('clock.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Start Times", className="box-title"),
                                        html.P("activity start times", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            scatter_start_time()
                        ]
                                  
                    ),
                ]
            ),

            #Troisième rangée de 4 Box j'ai tout simplement copié collé celle du dessus !

            html.Div(
                className="flex-container",  # Classe pour utiliser Flexbox
                children=[

                    #Item ou Box avec un donut qui correspondra aux total Hours par sport je pense 
                    html.Div(
                        className="box",
                        children=[html.Div(
                            className="box-header",
                            children=[
                                html.Img(src=dash.get_asset_url('trophy.svg'),className="box-icon"),
                                html.Div(
                                    children=[
                                        html.P("Records", className="box-title"),
                                        html.P("your top stats", className="box-subtitle")
                                    ]
                                )
                                
                            ]

                        ),
                        html.Div(
                            className="record-content",
                            children=[
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Top Speed", className="kudos-count"),
                                        html.P("72", className="kudos"),
                                        html.P("km/h",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Max Watts", className="kudos-count"),
                                        html.P("1200", className="kudos"),
                                        html.P("W",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Highest Heartrate", className="kudos-count"),
                                        html.P("210", className="kudos"),
                                        html.P("bpm",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Most Elevation Gain", className="kudos-count"),
                                        html.P("2300", className="kudos"),
                                        html.P("m",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Prs", className="kudos-count"),
                                        html.P("42", className="kudos"),
                                        html.P("prs",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Athletes", className="kudos-count"),
                                        html.P("900", className="kudos"),
                                        html.P("people",className="kudos-text")],
                                ),
                            ]
                        )
                                  ]
                    ),

                    #Un scatter avec hearthrate vs speed et avec une régréssion linéaire
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('watch.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Total Hours ", className="box-title"),
                                        html.P("total hours spent per sport", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            total_hours_donut()
                        ]
                    ),

                    #Une box avec 6 box représentant les records de l'année

                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('heart-pulse.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Heartrate vs. Speed", className="box-title"),
                                        html.P("heartrate compared to speed", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            scatter_hr_speed()
                            ]
                    ),

                    #Et un Bar chart représentant les élévation de l'année !
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('mountain.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Elevation", className="box-title"),
                                        html.P("total elevation per month", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            bar_elevation()
                        ]
                                  
                    ),
                ]
            ),
        ]
    )

    return dash_app
