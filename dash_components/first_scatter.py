import plotly.graph_objects as go
from dash import dcc
import numpy as np

def scatter_distance_power():

    distance=[20,30,35,25,47,58,39,78,90,120,58,50]
    power=[190,187,167,198,176,160,170,159,145,133,210,180]

    x=np.array(distance)
    y=np.array(power)
    a, b=np.polyfit(x,y, deg=1)

    x_trend=np.linspace(min(x),max(x),100)
    y_trend=a*x_trend+b

    figure=go.Figure()

    figure.add_trace(
        go.Scatter(
            mode="markers",
            marker=dict(
                size=7, 
                color='#5FB49C',
            ),
            name="Power vs. Distance",
            x=distance,
            y=power,
            showlegend=True,
        )
    )

    figure.add_trace(
        go.Scatter(
            mode='lines',
            x=x_trend,
            y=y_trend,
            line=dict(
                color='rgba(95, 180, 156, 0.6)', #couleur et opacité
                dash='dot',
                width=1.5,
            )
        )

    )
    figure.update_layout(
        #title="Power vs. Distance",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            #title="Distance",
            showgrid=False,
            showline=True,
            ticks='outside',
            tickcolor='white',
            ticklen=6,
            tickvals=[20,50,80,110,140,170,200],
            ticktext=['20km','50km','80km','110km','140km','170km','200km'],
            tickfont=dict(
                family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace',
                color='white',
            )
        ),
        yaxis=dict(
            range=[45,225],
            showgrid=False,
            showline=True,
            ticks='outside',
            tickcolor='white',
            ticklen=6,
            tickvals=[45,90,135,180,225],
            ticktext=['45w','90w','135w','180w','225w'],
            zeroline=True,
            tickfont=dict(
                color='white',
                family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace',
            ),

        ),
        margin=dict(t=30, b=30, l=40, r=10),
    )
    return dcc.Graph(
        id='First Scatter Plot',
        figure=figure,
        config={'displayModeBar':False, 'responsive':True},
        style={'width': '100%', 'height': '100%'}
    )