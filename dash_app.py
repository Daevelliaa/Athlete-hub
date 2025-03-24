import dash
from dash import html, dcc
from flask import session

def create_dash_app(flask_app):
    dash_app = dash.Dash(__name__,server=flask_app,routes_pathname_prefix='/dashboard/',)

    # On récupère le prénom depuis la session
    firstname = session.get('athlete', {}).get('firstname', 'Athlète')

    dash_app.layout = html.Div([
        html.H1(f"Bienvenue {firstname} 👋"),
        html.P("Voici ton interface interactive."),
        html.A("Se déconnecter", href="/logout", style={"color": "red", "font-weight": "bold"})
    ])

    return dash_app
