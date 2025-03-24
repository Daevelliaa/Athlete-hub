import plotly.graph_objs as go
import dash_core_components as dcc

def create_graphique():
    # Données des kilomètres parcourus chaque mois
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    kilometre = [900, 752, 810, 670, 530, 600, 720, 810, 650, 740, 800, 890]

    # Création de l'histogramme avec style SVG-like
    graphique = dcc.Graph(
        id='graphique-kilometres',
        figure={
            'data': [
                go.Bar(
                    x=mois,
                    y=kilometre,
                    name='Kilomètres parcourus',
                    marker={'color': 'red'},  # Couleur personnalisée pour les barres
                )
            ],
            'layout': go.Layout(
                title='Kilomètres parcourus par mois',
                title_x=0.5,  # Centrer le titre
                xaxis={
                    'title': 'Mois',
                    'tickvals': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                    'showgrid': False,  # Enlever les lignes de la grille
                    'zeroline': False,  # Enlever la ligne zéro
                    'showline': False   # Enlever la ligne de l'axe X
                },
                yaxis={
                    'title': 'Kilomètres',
                    'showgrid': True,  # Garder la grille pour l'axe Y
                    'zeroline': False,  # Enlever la ligne zéro
                },
                plot_bgcolor='rgba(0, 0, 0, 0)',  # Fond transparent pour un effet "image"
                paper_bgcolor='rgba(0, 0, 0, 0)',  # Fond transparent pour l'ensemble du graphique
                showlegend=False,  # Enlever la légende
                margin=dict(t=50, b=50, l=50, r=50),  # Marges autour du graphique
            )
        },
        config={'displayModeBar': False}  # Désactiver la barre de mode Plotly
    )
    return graphique
