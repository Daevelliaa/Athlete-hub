import plotly.graph_objects as go
import numpy as np
import pandas as pd
from dash import no_update

def scatter_temp_speed(df):
    df = df.copy()

    if df.empty or 'average_temp' not in df.columns or 'average_speed' not in df.columns:
        return no_update

    # 🎯 Filtrer uniquement les Rides avec température disponible
    df_ride = df[
        (df['type'] == 'Ride') &
        df['average_temp'].notnull() &
        df['average_speed'].notnull()
    ]

    # Conversion m/s → km/h
    df_ride['speed_kmh'] = df_ride['average_speed'] * 3.6
    df_ride['temp'] = df_ride['average_temp']

    # Si pas assez de points, ne rien afficher
    if df_ride.empty or len(df_ride) < 2:
        return go.Figure()

    # ➕ Régression linéaire
    x = np.array(df_ride['temp'])
    y = np.array(df_ride['speed_kmh'])
    a, b = np.polyfit(x, y, deg=1)
    x_trend = np.linspace(min(x), max(x), 100)
    y_trend = a * x_trend + b

    # 📈 Scatter
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        mode="markers",
        x=df_ride['temp'],
        y=df_ride['speed_kmh'],
        marker=dict(size=7, color='#5FB49C'),
        name="Speed vs. Temp",
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        mode='lines',
        x=x_trend,
        y=y_trend,
        line=dict(color='rgba(95, 180, 156, 0.6)', dash='dot', width=1.5),
        showlegend=False
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            #title="Température (°C)",
            showgrid=False,
            showline=True,
            ticks='outside',
            tickcolor='white',
            tickfont=dict(color='white', family='monospace'),
            zeroline=False,
            tickvals=[0, 5, 10, 15, 20, 25, 30],
            ticktext=['0°C', '5°C', '10°C', '15°C', '20°C', '25°C', '30°C'],
        ),
        yaxis=dict(
            #title="Vitesse moyenne (km/h)",
            range=[10, 50],  # ajustable
            tickvals=[10, 20, 30, 40, 50],
            ticktext=['10 km/h', '20 km/h', '30 km/h', '40 km/h', '50 km/h'],
            showgrid=False,
            showline=True,
            ticks='outside',
            tickcolor='white',
            tickfont=dict(color='white', family='monospace'),
            zeroline=False,
        ),
        font=dict(color='white'),
        margin=dict(t=30, b=30, l=40, r=10)
    )

    return fig
