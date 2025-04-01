import plotly.graph_objects as go
from dash import dcc
import pandas as pd

def create_donut_graphique(df):

    df=df.copy()
    df['start_date']=pd.to_datetime(df['start_date'])
    df["start_date"]=df['start_date'].dt.date

    active_days=len(set(df['start_date']))
    rest_days=365-active_days

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

    return figure

