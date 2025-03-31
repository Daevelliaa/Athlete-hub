import plotly.graph_objects as go
from dash import dcc

def total_hours_donut(ride_hours=200, virtual_ride_hours=100, run_hours=150):
    labels = ['Ride', 'VirtualRide', 'Run']
    values = [ride_hours, virtual_ride_hours, run_hours]
    colors = ['#5FB49C', '#0C7489', '#16324F']  # Tu peux adapter à ton thème

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
        sort=False  # Pour garder l'ordre donné
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
            y=-0.1
        ),
        margin=dict(t=80, b=80, l=80, r=80)
    )

    return dcc.Graph(
        id='total-hours-donut-chart',
        figure=figure,
        config={'displayModeBar': False, 'responsive': True},
        style={'height': '100%', 'width': '100%'}
    )
