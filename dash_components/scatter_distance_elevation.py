import plotly.graph_objects as go
import numpy as np
import pandas as pd
from dash import no_update

def scatter_distance_elevation(df):
    df = df.copy()

    # Filtrer les types et données valides
    df = df[
        df['type'].isin(['Run', 'Ride', 'VirtualRide']) &
        df['distance'].notnull() &
        df['total_elevation_gain'].notnull()
    ]

    df['distance_km'] = df['distance'] / 1000
    df['elevation_m'] = df['total_elevation_gain']

    # Trend line (régression linéaire)
    x = df['distance_km'].values
    y = df['elevation_m'].values

    if len(x) < 2:
        return no_update  # pas assez de points

    a, b = np.polyfit(x, y, 1)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = a * x_line + b

    fig = go.Figure()

    # Extrait le max de distance
    max_distance = df['distance_km'].max()
    x_max = np.ceil(max_distance / 10) * 10  # arrondi supérieur à la dizaine

    # Ticks tous les 10 km jusqu’au max
    x_tickvals = list(np.arange(0, x_max + 1, 20))
    x_ticktext = [f"{v:.0f}km" for v in x_tickvals]


    max_elev = df['elevation_m'].max()
    y_max = np.ceil(max_elev / 500) * 500  # arrondi aux 500 m

    # Ticks tous les 500 m jusqu’au max
    y_tickvals = list(np.arange(0, y_max + 1, 500))
    y_ticktext = [f"{v:.0f} m" for v in y_tickvals]




    # Points
    fig.add_trace(go.Scatter(
        mode='markers',
        x=df['distance_km'],
        y=df['elevation_m'],
        marker=dict(size=7, color='#5FB49C', opacity=0.8),
        name="Sorties"
    ))

    # Courbe de tendance
    fig.add_trace(go.Scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        line=dict(color='rgba(255,255,255,0.3)', dash='dot', width=2),
        name="Tendance"
    ))

    # Layout stylé
    fig.update_layout(
        #title="Distance vs. Dénivelé",
        xaxis=dict(
            #title="Distance (km)",
            tickvals=x_tickvals,
            ticktext=x_ticktext,
            tickfont=dict(color='white', family='monospace'),
            showgrid=False,
            linecolor='white',
            ticks='outside',
            tickcolor='white',
            zeroline=False,
        ),
        yaxis=dict(
            #title="Dénivelé (m)",
            tickvals=y_tickvals,
            ticktext=y_ticktext,
            tickfont=dict(color='white', family='monospace'),
            showgrid=False,
            linecolor='white',
            ticks='outside',
            tickcolor='white',
            zeroline=False,
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        showlegend=False,
        margin=dict(t=30, b=30, l=50, r=20)
    )

    return fig
