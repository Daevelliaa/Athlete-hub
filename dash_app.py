import dash
from dash import html
from dash_components.first_graphique import create_graphique
from dash_components.donut_chart import create_donut_graphique
from dash_components.heatmap import generate_daily_heatmap
from dash_components.first_scatter import scatter_distance_power

def create_dash_app(flask_app):
    # Assurez-vous que Dash est correctement configuré avec Flask
    dash_app = dash.Dash(__name__,server=flask_app,routes_pathname_prefix='/dashboard/',)
    

    # Définir la mise en page de Dash
    dash_app.layout = html.Div(
        id='dash-container',  # Appliquer une classe CSS style.css stocké dans assets
        children=[
            # Titre de la page
            html.P("Bienvenue dans ton Dashboard", style={"text-align": "left"}),


            # Div principale qui contient les 4 boîtes
            html.Div(
                className="flex-container",  # Classe pour utiliser Flexbox
                children=[
                    html.Div(
                        className="box1",
                        children=[]#generate_daily_heatmap()
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
                                        html.P("Total Hours", className="box-title"),
                                        html.P("total distance per month", className="box-subtitle"),
                                    ])
                                ]
                            ),
                            html.Div(
                                children=create_graphique(),
                                className="graph-container",
                            )
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
                            create_donut_graphique()
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
                                        html.P("993", className="kudos"),
                                        html.P("kudos",className="kudos-text")],
                                ),
                                html.Div(
                                    className="social-content-item",
                                    children=[
                                        html.P("Comment Count", className="kudos-count"),
                                        html.P("145", className="kudos"),
                                        html.P("comments",className="kudos-text")],
                                )
                            ]
                        )
                                  ]
                    ),

                    #Le graph scatter avec power vs distance
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
                            scatter_distance_power()
                        ]
                    ),
                    html.Div(
                        className="box",
                        children=[html.P("Graphiques à venir ici", style={"color": "white"})]
                    ),
                    html.Div(
                        className="box",
                        children=[html.P("Graphiques à venir ici", style={"color": "white"})]
                    ),
                ]
            ),
        ]
    )

    return dash_app
