import dash
from dash import html, dcc

from datetime import date, datetime
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
            #dcc.Store(id="activities_2024"),
            html.Div(
                style={
                    'display': 'flex',
                    'justifyContent': 'space-around',
                    'alignItems': 'center',
                    },
                    children=[
                        html.P(id='welcome-text', style={"text-align": "left"}),
                        #dcc.Dropdown(
                            #id='year-selector',
                            #options=[{'label': str(year), 'value': year} for year in range(2018, 2026)],
                            #value=2024,
                            #placeholder="Choisir une année",
                            #clearable=False,
                            #style={
                                #'width': '200px',
                                #'color': 'black'    
                                #},
            #),
            #html.Label("Sélectionne une plage de dates :"),
            dcc.DatePickerRange(
                id='date-range-picker',
                max_date_allowed=datetime.today().date(),
                min_date_allowed=date(2018,1,1),
                start_date=date(2024, 1, 1),
                end_date=date(2025,1,1),
                display_format='DD/MM/YYYY'
    ),
            dcc.Store(id='yearly_activities_store'),

                    ]
            ),
            
            


            # Div principale qui contient les 4 boîtes
            html.Div(
                className="flex-container",  # Classe pour utiliser Flexbox
                children=[
                    html.Div(
                        className="box1",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('calendar-days.svg'), className="box-icon"),
                                    html.Div([
                                        html.P("Daily Activities", className="box-title"),
                                        html.P("hours per day of activities", className="box-subtitle"),
                                        ]),
                                        html.Div(
                                            className="box-dropdown",
                                            children=[
                                                dcc.Dropdown(
                                                    id='year-selector',
                                                    options=[{'label': str(y), 'value': y} for y in range(2018, 2026)],
                                                    value=2024,
                                                    clearable=False,
                                                    style={'width': '200px', 'color': 'black'}
                                        ),

                                            ]
                                        ),
                                        
                                        dcc.Store(id='year'),
                                    ]
                                
                            ),
                            dcc.Graph(
                                id='heatmap-container',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'visibility': 'hidden'}
                            ),

                        ]
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
                            dcc.Graph(
                                id='Scatter_start',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'},

                            ),
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
                                        html.P("",id='top_speed', className="kudos"),
                                        html.P("km/h",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Max Watts", className="kudos-count"),
                                        html.P("",id="max_watts", className="kudos"),
                                        html.P("W",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Highest Heartrate", className="kudos-count"),
                                        html.P("",id="highest_heartrate", className="kudos"),
                                        html.P("bpm",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Most Elevation Gain", className="kudos-count"),
                                        html.P("",id="most_elevation", className="kudos"),
                                        html.P("m",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Prs", className="kudos-count"),
                                        html.P("",id="pr", className="kudos"),
                                        html.P("prs",className="kudos-text")],
                                ),
                                html.Div(
                                    className="record-content-item",
                                    children=[
                                        html.P("Kilojoules", className="kudos-count"),
                                        html.P("",id="athlete", className="kudos"),
                                        html.P("kj lost",className="kudos-text")],
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
                            dcc.Graph(
                                id='donut_total_hours',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'},
                            ),
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
                            dcc.Graph(
                                id="scatter_hr_speed",
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'},
                            )
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
                                        html.P("Elevation (m)", className="box-title"),
                                        html.P("total elevation per month", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='elevation',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'},
                            )
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
                                html.Img(src=dash.get_asset_url('file-badge-2.svg'),className="box-icon"),
                                html.Div(
                                    children=[
                                        html.P("Biggest Activity", className="box-title"),
                                        html.P("", className="box-subtitle")
                                    ]
                                ),
                                
                            ]

                        ),
                        html.P(id='map-title', className='map-title'),
                        dcc.Graph(
                            id='map',
                            config={'displayModeBar': False, 'responsive': True},
                            style={'width': '100%', 'height': '100%', 'visibility': 'hidden'},
                        ),
                        html.Div(
                            id='map-infos',
                            className='map-infos-container',
                            children=[
                                html.P(id='map-distance',className='map-info'),
                                html.P(id='map-elevation',className='map-info'),
                                 html.P(id='map-speed',className='map-info'),
                            ]

                        ),
                        
                        
                                  ]
                    ),

                    #Le graph scatter avec power vs distance et la régréssion linéaire très stylé
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('biceps-flexed.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Activity count", className="box-title"),
                                        html.P("number of activities per month", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='activity-count',
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
                                    html.Img(src=dash.get_asset_url('ruler.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Distance Ranges", className="box-title"),
                                        html.P("number of activities within a distance range", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='range-donut',
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
                                    html.Img(src=dash.get_asset_url('thermometer-sun.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Temp vs. Speed", className="box-title"),
                                        html.P("avg temperature per avg speed", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='scatter-temp',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'},

                            ),
                        ]
                                  
                    ),
                ]
            ),
            # Div principale qui contient les 4 boîtes
            html.Div(
                className="flex-container2",  # Classe pour utiliser Flexbox
                children=[
                    
                    #Le radar chart avec les heartrate zone
                    html.Div(
                        className="box",
                        children=[
                            html.Div(
                                className="box-header",
                                children=[
                                    html.Img(src=dash.get_asset_url('activity.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Heartrate Zones (avg)", className="box-title"),
                                        html.P("total hours spent in each zone", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='radar',
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
                                    html.Img(src=dash.get_asset_url('chart-no-axes-combined.svg'),className="box-icon"),
                                    html.Div([
                                        html.P("Distance vs. Elevation", className="box-title"),
                                        html.P("elevation gained per distance", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            dcc.Graph(
                                id='scatter-elevation',
                                config={'displayModeBar': False, 'responsive': True},
                                style={'width': '100%', 'height': '100%', 'visibility': 'hidden'}
                            ),
                            ]
                    ),
                ]
            ),
                        
        ]
    )

    return dash_app
