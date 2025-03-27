import plotly.graph_objects as go 
from dash import dcc

def scatter_pr():

    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    pr=[100,50,120,59,48,36,75,89,76,141,15,21]

    figure=go.Figure()

    figure.add_trace(
        go.Scatter(
            x=mois,
            y=pr,
            mode="lines+markers+text",
            text=pr,
            textposition='top center',
            textfont=dict(
                color='white',
                size=10,
            ),
            line=dict(
                shape='hvh',
                width=2,
                color='#5FB49C',
            ),
            marker=dict(
                size=5,
                color='white',
            )
        )
    )

    figure.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            showline=True,
            tickvals=[0,3,6,9],
            ticktext=["Janvier","Avril","Juillet","Octobre"],
            tickfont=dict(
                color="white",
                family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace',
            ),
            ticks='outside',
            ticklen=6,
            tickcolor='white',
        
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
        ),
        margin=dict(t=30, b=30, l=30, r=30),

    )

    return dcc.Graph(
        figure=figure, 
        config={'displayModeBar':False, 'responsive':True},
        style={'width': '100%', 'height': '100%'}
    )
