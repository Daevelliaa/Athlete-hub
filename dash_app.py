import dash
from dash import html
from dash_components.first_graphique import create_graphique
from dash_components.donut_chart import create_donut_graphique
from dash_components.heatmap import generate_daily_heatmap

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
                        children=[generate_daily_heatmap()]
                    ),
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
                            create_graphique()
                        ]
                    ),
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
                        )
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
                    html.Div(
                        className="box",
                        children=[html.P("Graphiques à venir ici", style={"color": "white"})]
                    ),
                ]
            ),
        ]
    )

    return dash_app
