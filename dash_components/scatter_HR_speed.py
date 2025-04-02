import plotly.graph_objects as go
import numpy as np
import pandas as pd

def scatter_hr_speed(df):
    df = df.copy()

    # Filtrer uniquement les activités de type "Run"
    df_run = df[df['type'] == 'Run']

    # Supprimer les vitesses et fréquences cardiaques nulles ou absentes
    df_run = df_run[
        df_run['average_speed'].notnull() & 
        (df_run['average_speed'] > 0) & 
        df_run['average_heartrate'].notnull() & 
        (df_run['average_heartrate'] > 0)
    ]

    # Conversion des vitesses de m/s à km/h
    df_run['average_speed'] = df_run['average_speed'] * 3.6

    # Extraire les données en array
    x = np.array(df_run['average_speed'])
    y = np.array(df_run['average_heartrate'])

    # Vérification : au moins 2 points pour faire une régression
    if len(x) < 2:
        return go.Figure()

    # Régression linéaire : y = ax + b
    a, b = np.polyfit(x, y, deg=1)

    # Courbe de tendance étendue
    x_trend = np.linspace(x.min(), x.max(), 100)
    y_trend = a * x_trend + b

    # Création du graphique
    figure = go.Figure()

    # Nuage de points
    figure.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name="HeartRate vs. Speed",
            marker=dict(size=7, color='#5FB49C'),
        )
    )

    # Courbe de régression
    figure.add_trace(
        go.Scatter(
            x=x_trend,
            y=y_trend,
            mode='lines',
            name="Régression linéaire",
            line=dict(
                color='rgba(95, 180, 156, 0.6)',
                dash='dot',
                width=1.5,
            )
        )
    )

    # Mise en forme du layout
    figure.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            zeroline=False,
            showgrid=False,
            showline=True,
            ticks='outside',
            tickcolor='white',
            ticklen=6,
            tickvals=[5,7,9,11,13,15,17],
            ticktext=['5km/h','7km/h','9km/h','11km/h','13km/h','15km/h','17km/h'],
            tickfont=dict(
                color='white',
                family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace',
            )
        ),
        yaxis=dict(
            zeroline=False,
            range=[45, 225],
            showgrid=False,
            showline=True,
            ticks='outside',
            tickcolor='white',
            ticklen=6,
            tickvals=[45, 90, 135, 180, 225],
            ticktext=['45bpm','90bpm','135bpm','180bpm','225bpm'],
            tickfont=dict(
                color='white',
                family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace',
            )
        ),
        margin=dict(t=30, b=30, l=40, r=10),
    )

    return figure
