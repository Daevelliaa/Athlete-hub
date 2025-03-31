import plotly.graph_objs as go
from dash import dcc

def bar_elevation():
    # Données des kilomètres parcourus chaque mois
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    kilometre = [1600, 1546, 5963, 6301, 5305, 6006, 7208, 8104, 6506, 7405, 8010, 8960]

    figure=go.Figure(
        data=[go.Bar(
            name='mois vs kilomètres',
            text=kilometre,
            x=mois,
            y=kilometre,
            textposition='outside',
            marker=dict(color='#5FB49C',line=dict(color='black',width=0.5)),
            textfont=dict(color='white',family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace', size=15),
            opacity=0.8
        )]
    )
    figure.update_layout(
        barcornerradius=5,
        xaxis=dict(
            tickvals=[2, 5, 8, 11],
            ticktext=['Mars', 'Juin', 'Septembre', 'Décembre'],
            showgrid=False,
            zeroline=False,
            showline=True,
            linecolor='white',
            tickangle=0,
            tickfont=dict(color='white',family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace'),
            ticks='outside',
            ticklen=6,
            tickcolor='white',
        ),
        yaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False,
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        showlegend=False,
        margin=dict(t=60, b=30, l=30, r=30),
    )
    return dcc.Graph(
        id='Bar_elevation',
        figure=figure,
        config={'displayModeBar': False, 'responsive':True},
        style={'width': '100%', 'height': '100%'} #responsive donc toute la taille de la box 
    )


