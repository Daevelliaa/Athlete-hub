import plotly.graph_objects as go
from dash import dcc
import numpy as np
from datetime import datetime, date
import calendar

def heatmap():

    year=2022
    today=datetime(year,1,1)
    today1=datetime(year,12,31)
    offset=today.weekday()
    offset1=today1.weekday()

    # Créer la première semaine
    first_week = np.random.randint(0, 11, size=7 - offset).tolist() + [None] * offset

    # Créer les 50 semaines complètes
    middle_weeks = [np.random.randint(0, 11, size=7).tolist() for _ in range(51)]

    # Créer la dernière semaine
    last_week = [None] * (6 - offset1) + np.random.randint(0, 11, size=offset1 + 1).tolist()  

    z=[first_week] + middle_weeks + [last_week]  #quand on met les crochets la liste est transformé en sous liste
        
    z=np.transpose(z)

    figure=go.Figure()

    figure.add_trace(
        go.Heatmap(
            colorscale=['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353'],
            z=z,
            hoverongaps=True,
            showscale=False,
            xgap=4,
            ygap=4,

        )
    )

    figure.update_layout(
        shapes=[
            dict(type="line", x0=3.5, x1=3.5, y0=-0.5, y1=6.5, line=dict(width=2, color="white")),
            dict(type="line", x0=7.5, x1=7.5, y0=-0.5, y1=6.5, line=dict(width=2, color="white")),
            dict(type="line", x0=11.5, x1=11.5, y0=-0.5, y1=6.5, line=dict(width=2, color="white")),
            dict(type="line", x0=15.5, x1=15.5, y0=-0.5, y1=6.5, line=dict(width=2, color="white")),
            dict(type="line", x0=19.5, x1=19.5, y0=-0.5, y1=6.5, line=dict(width=2, color="white")),
        ],
        yaxis=dict(showgrid=False, showline=False, zeroline=False, showticklabels=False),
        margin=(dict(t=170,b=170,l=5,r=5)),
        title='Ma première Heatmap',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    figure.update_xaxes(
    side="top",                        # place les labels en haut
    tickmode="array",                 # on définit manuellement les positions
    tickvals=[1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45],  # semaines de début de mois (à ajuster selon ton calendrier !)
    ticktext=["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"],
    tickfont=dict(color="white", size=12),
    showline=False,
    showgrid=False,
    zeroline=False
)


    return dcc.Graph(
        figure=figure,
        config={'displayModeBar':False,'responsive':True},
    )

