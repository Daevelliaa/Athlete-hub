import plotly.graph_objs as go
from dash import dcc

def create_graphique():
    # Données des kilomètres parcourus chaque mois
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    kilometre = [900, 752, 810, 670, 530, 600, 720, 810, 650, 740, 800, 890]

    # Création de l'histogramme avec style SVG-like
    graphique = dcc.Graph(
        id='graphique-kilometres',
        figure={
            'data': [go.Bar(x=mois,
                            y=kilometre,
                            name='Kilomètres parcourus',
                                
                            text=kilometre,
                            textposition='outside',
                            textfont=dict(size=15,color='white', family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace'),
                            marker=dict(color='#5FB49C',line=dict(color='black',width=0.5)),
                            opacity=0.9
                            )],
            'layout': go.Layout(
                barcornerradius=5,
                xaxis={
                    
                    'tickvals': [0, 3, 6, 9,],
                    'showgrid': False,  # Enlever les lignes de la grille
                    'zeroline': False,  # Enlever la ligne zéro
                    'showline': True,  # Enlever la ligne de l'axe X
                    'linecolor':'white',
                    'ticktext':['Janvier', 'Avril', 'Juillet', 'Octobre'],
                    'tickangle':0,
                    'tickfont':dict(color='white',family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace'),
                    'ticks':'outside',
                    'ticklen':6,
                    'tickcolor':'white',
                },
                yaxis={
                    'showticklabels': False,
                    'showgrid': False,  # Enlever la grille pour l'axe Y
                    'zeroline': False,  # Enlever la ligne zéro
                },
                plot_bgcolor='rgba(0, 0, 0, 0)',  # Fond transparent pour un effet "image"
                paper_bgcolor='rgba(0, 0, 0, 0)',  # Fond transparent pour l'ensemble du graphique
                showlegend=False,  # Enlever la légende
                margin=dict(t=60, b=30, l=30, r=30),  # Marges autour du graphique
            )
        },
        config={'displayModeBar': False}  # Désactiver la barre de mode Plotly
    )
    return graphique
