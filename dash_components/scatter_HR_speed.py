import plotly.graph_objects as go
from dash import dcc
import numpy as np

def scatter_hr_speed():

    speed=[10,9,11.5,10,9.5,8.3,13.6,14.5,9.6,10.3,12.6,15]
    hr=[145,123,156,142,136,123,170,180,110,136,156,180]

    x=np.array(speed)
    y=np.array(hr)
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
            name="HeartRate vs. Speed",
            x=speed,
            y=hr,
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
            tickvals=[5,7,9,11,13,15,17],
            ticktext=['5km/h','7km/h','9km/h','11km/h','13km/h','15km/h','17km/h'],
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
            ticktext=['45bpm','90bpm','135bpm','180bpm','225bpm'],
            zeroline=True,
            tickfont=dict(
                color='white',
                family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace',
            ),

        ),
        margin=dict(t=30, b=30, l=40, r=10),
    )
    return dcc.Graph(
        id='Scatter HeartRate vs Speed',
        figure=figure,
        config={'displayModeBar':False, 'responsive':True},
        style={'width': '100%', 'height': '100%'}
    )