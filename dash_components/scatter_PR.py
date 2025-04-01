import plotly.graph_objects as go 
from dash import dcc
import pandas as pd

def scatter_pr(df):

    df=df.copy()
    # Assure-toi que la colonne est bien datetime
    df['start_date'] = pd.to_datetime(df['start_date'])

    # Optionnel : filtrer uniquement l'année 2024
    df_2024 = df[df['start_date'].dt.year == 2024]

    # Extraire le mois et on créé une colonne avec les mois 1 à 12
    df_2024['month'] = df_2024['start_date'].dt.month

    # Grouper par mois et sommer les pr_count
    monthly_pr = df_2024.groupby('month')['pr_count'].sum()

    # Assure que tous les mois sont présents (même avec 0 PR)
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
    return figure
