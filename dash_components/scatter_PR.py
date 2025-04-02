import plotly.graph_objects as go 
from dash import dcc
import pandas as pd

def scatter_pr(df):

    df = df.copy()

    # S'assurer que la colonne est en datetime
    df['start_date'] = pd.to_datetime(df['start_date'])

    # Extraire le mois dans une nouvelle colonne
    df['month'] = df['start_date'].dt.month

    # Grouper par mois et sommer les pr_count
    monthly_pr = df.groupby('month')['pr_count'].sum()

    # Remplir les mois manquants avec 0
    monthly_pr = monthly_pr.reindex(range(1, 13), fill_value=0)



    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    figure=go.Figure()

    figure.add_trace(
        go.Scatter(
            x=mois,
            y=monthly_pr.values,
            mode="lines+markers+text",
            text=monthly_pr.values,
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
            zeroline=False,
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
            zeroline=False,
            showgrid=False,
            showline=False,
            showticklabels=False,
        ),
        margin=dict(t=30, b=30, l=30, r=30),

    )
    return figure
