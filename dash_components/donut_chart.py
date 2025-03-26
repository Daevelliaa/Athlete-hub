import plotly.graph_objects as go
from dash import dcc

def create_donut_graphique(active_days=234, rest_days=131):
    figure = go.Figure(
        data=[go.Pie(labels=['active', 'rest'],
            values=[active_days, rest_days],
            hole=0.6,
            textinfo='value',
            textposition='outside',
            marker=dict(colors=['#5FB49C', '#1B2A38'],line=dict(color='white', width=1)),
            domain=dict(x=[0.2, 0.8], y=[0.1, 0.7])
        )]
    )

    figure.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0,0,0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(orientation='h',x=0.5,xanchor='center',y=-0.1),
        margin=dict(t=20, b=20, l=20, r=20)
    )

    # ⬇️ On retourne directement le composant Dash prêt à être affiché
    return dcc.Graph(
        id='donut-chart',
        figure=figure,
        config={'displayModeBar': False, 'responsive':True},
        style={'height': '100%', 'width': '100%'}
    )
