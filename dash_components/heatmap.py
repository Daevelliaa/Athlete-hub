from dash import dcc
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def generate_daily_heatmap():
    # 1. Générer les dates
    dates = pd.date_range(start='2024-01-01', end='2024-12-31')

    # 2. Générer des données fictives
    np.random.seed(42)
    durations = np.random.uniform(0, 3, size=len(dates))

    # 3. Créer le DataFrame
    df = pd.DataFrame({'date': dates, 'duration': durations})
    df['dow'] = df['date'].dt.weekday     # day of week (0=lundi, 6=dimanche)
    df['week'] = df['date'].dt.isocalendar().week
    df['week'] = df['week'] - df['week'].min()  # pour commencer à 0

    # 4. Pivot pour créer la grille
    pivot = df.pivot_table(index='dow', columns='week', values='duration', aggfunc='sum')

    # 5. Créer la figure Plotly
    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns,
        y=['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
        colorscale=[
            [0.0, "#1a1a1a"],
            [0.25, "#33691E"],
            [0.5, "#558B2F"],
            [0.75, "#76FF03"],
            [1.0, "#CCFF90"]
        ],
        xgap=2,  # ➕ simulate border
        ygap=2,  # ➕ simulate border
        showscale=False,
        hovertemplate="Semaine %{x}, %{y} <br>Durée: %{z:.1f}h<extra></extra>"
    ))

    fig.update_layout(
        title='Daily Activity Heatmap (fictive)',
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0,0,0)',
        font=dict(color='white'),
        margin=dict(l=20, r=20, t=170, b=170),
        height=260
    )

    # 6. Retourner le dcc.Graph prêt à afficher
    return dcc.Graph(
        id='daily-heatmap',
        figure=fig,
        config={'displayModeBar': False},
        style={'width': '100%', 'height': '100%'}
    )