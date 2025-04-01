import plotly.graph_objects as go 
from dash import dcc
import pandas as pd

def scatter_start_time(df):

    df=df.copy()
    df['start_date']=pd.to_datetime(df['start_date'])
    df_hour=df['start_date'].dt.hour

    hour_counts=df_hour.value_counts().sort_index()
    hour_counts = hour_counts.reindex(range(24), fill_value=0)

    mois = hour_counts.index
    pr=hour_counts.values

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
    return figure
