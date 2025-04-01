import plotly.graph_objs as go
from dash import dcc
import pandas as pd

def create_graphique(df):
    #ajouter une colonne mois au dataframe des activités
    df=df.copy()
    df['start_date']=pd.to_datetime(df['start_date'])
    df['mois']=df['start_date'].dt.month

    # Grouper les distances par mois
    monthly_km = df.groupby('mois')['distance'].sum() / 1000  # m → km
    
    # Données des kilomètres parcourus chaque mois
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    y_values = [monthly_km.get(i, 0) for i in range(1, 13)]
    text_values = [str(int(km)) for km in y_values]

    figure=go.Figure()

    figure.add_trace(go.Bar(
          name='mois vs kilomètres',
          text=text_values,
          x=mois,
          y=y_values,
          textposition='outside',
          marker=dict(color='#5FB49C',line=dict(color='black',width=0.5)),
          textfont=dict(color='white',family='SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace', size=15),
          opacity=0.8

    ))
        
    figure.update_layout(
        barcornerradius=5,
        xaxis=dict(
            tickvals=[0, 3, 6, 9],
            ticktext=['Janvier', 'Avril', 'Juillet', 'Octobre'],
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
    return figure
        


