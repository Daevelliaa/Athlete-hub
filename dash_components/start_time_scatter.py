import plotly.graph_objects as go 
from dash import dcc

def scatter_start_time():

    mois = list(range(24))
    pr=[0,0,0,0,0,0,5,8,15,26,41,31,32,45,12,16,13,56,43,13,10,9,4,0]

    figure=go.Figure()

    figure.add_trace(
        go.Scatter(
            x=mois,
            y=pr,
            fill="tozeroy",
            mode="lines+text",
            text=pr,
            textposition='top center',
            textfont=dict(
                color='white',
                size=10,
            ),
            line=dict(
                width=2,
                color='#5FB49C',
                shape='spline',
            ),
        )
    )

    figure.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            range=[-1, 24],
            showgrid=False,
            zeroline=False,
            showline=True,
            tickvals=[0,1,2,3,4,5,6,7,8,9,11,13,15,17,19,21,23],
            #ticktext=["Janvier","Avril","Juillet","Octobre"],
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
