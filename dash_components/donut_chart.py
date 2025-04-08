import plotly.graph_objects as go
import pandas as pd

def create_donut_graphique(df):
    df = df.copy()
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['start_date'] = df['start_date'].dt.date

    # Calculer les bornes de la période sélectionnée
    start = df['start_date'].min()
    end = df['start_date'].max()
    total_days = (end - start).days + 1  # +1 pour inclure le jour de début

    # Jours actifs = nb de jours uniques avec activité
    active_days = len(set(df['start_date']))

    # Jours sans activité
    rest_days = total_days - active_days

    # Création du donut
    figure = go.Figure(
        data=[go.Pie(
            labels=['Active days', 'Rest days'],
            values=[active_days, rest_days],
            hole=0.6,
            textinfo='value',
            textposition='outside',
            marker=dict(colors=['#5FB49C', '#1B2A38'], line=dict(color='white', width=1)),
            domain=dict(x=[0.2, 0.8], y=[0.1, 0.7]),
            pull=[0.05]*5  # effet stylé qui écarte les parts
        )]
    )

    # Mise en forme
    figure.update_layout(
        #title=f"Activité sur {total_days} jours",
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0,0,0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(orientation='h', x=0.5, xanchor='center', y=-0.1),
        margin=dict(t=30, b=20, l=20, r=20)
    )

    return figure
