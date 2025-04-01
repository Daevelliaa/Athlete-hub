import plotly.graph_objects as go
from dash import dcc
import numpy as np

def scatter_distance_power(df):
    
    df=df.copy()
    df_ride=df[df['type'].isin(['Ride','VirtualRide'])]
    #on enlève toutes les datas ou il n'y a pas de average watts
    df_ride = df_ride[df_ride['average_watts'].notnull() & (df_ride['average_watts'] > 0)]
    df_ride['distance']=df['distance']/1000


    x=np.array(df_ride['distance'])
    y=np.array(df_ride['average_watts'])
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
            x=df_ride['distance'],
            y=df_ride['average_watts'],
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
    return figure