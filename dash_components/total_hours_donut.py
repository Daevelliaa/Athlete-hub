import plotly.graph_objects as go
from dash import dcc
import pandas as pd

def total_hours_donut(df):

    df=df.copy()
    # Étape 2 : Grouper par type d’activité et faire la somme
    time_by_activity = (df.groupby('type')['moving_time'].sum()/3600).astype(int)

    # Optionnel : trier du plus long au plus court
    time_by_activity = time_by_activity.sort_values(ascending=False)

    labels = time_by_activity.index.tolist()
    values = time_by_activity.values.tolist()

    custom_colors = [
    "#5FB49C",  # vert pastel
    "#0C7489",  # bleu pétrole
    "#16324F",  # bleu foncé
    "#F4D06F",  # jaune moutarde
    "#FF6F59",  # rouge corail
    "#885053",  # vieux rose
    "#96ADC8",  # lavande froide
    "#2A2D34",  # noir bleuté
    "#E8DAB2",  # beige clair
    "#C8553D",  # terre cuite
]
    colors = custom_colors[:len(labels)]

    figure = go.Figure()

    figure.add_trace(go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        textinfo='value',
        textposition='outside',
        marker=dict(
            colors=colors,
            line=dict(color='white', width=1)
        ),
        sort=False,
        domain=dict(x=[0.2, 0.8], y=[0.1, 0.8])  #le domaine du donut de la figure
    ))

    figure.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            orientation='h',
            x=0.5,
            xanchor='center',
            y=-0.2,
            traceorder='normal',      # ✅ Assure l’ordre logique (important !)
            font=dict(size=11),
            itemwidth=40,             # ✅ Largeur max par item
            valign='middle'
        ),
        margin=dict(t=20, b=20, l=20, r=20)
    )

    return figure
