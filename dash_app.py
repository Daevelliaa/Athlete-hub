import dash
from dash import html
from dash_components.first_graphique import create_graphique

def create_dash_app(flask_app):
    # Assurez-vous que Dash est correctement configuré avec Flask
    dash_app = dash.Dash(
        __name__,
        server=flask_app,  # Relie Dash au serveur Flask existant
        routes_pathname_prefix='/dashboard/',  # Chemin d'URL de l'application Dash
    )

    graphique = create_graphique()

    # Définir la mise en page de Dash
    dash_app.layout = html.Div(
        id='dash-container',  # Appliquer une classe CSS
        children=[
            # Titre de la page
            html.P("Bienvenue dans ton Dashboard", style={"text-align": "left"}),


            # Div principale qui contient les 4 boîtes
            html.Div(
                className="flex-container",  # Classe pour utiliser Flexbox
                children=[
                    html.Div(
                        className="box1",
                        children=[html.P("Graphiques à venir ici", style={"color": "white"})]
                    ),
                    html.Div(
                        className="box",
                        children=[graphique]
                    ),
                    html.Div(
                        className="box",
                        children=[html.P("Graphiques à venir ici", style={"color": "white"}),
                                  html.A("Se déconnecter",href="/logout",style={"color":"red","font-weight": "bold"})
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
                    html.Div(
                        className="box",
                        children=[html.P("Graphiques à venir ici", style={"color": "white"})]
                    ),
                ]
            ),
        ]
    )

    return dash_app
