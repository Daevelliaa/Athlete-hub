import plotly.graph_objs as go
import pandas as pd

def create_graphique(df):
    df = df.copy()
    df['start_date'] = pd.to_datetime(df['start_date'])

    # Déterminer la durée sélectionnée
    start = df['start_date'].min()
    end = df['start_date'].max()
    days = (end - start).days

    # Déterminer la fréquence d’agrégation
    if days <= 14:
        df['periode'] = df['start_date'].dt.date  # par jour
        x_labels = df['periode'].sort_values().unique()
        #title = "Distance quotidienne"
    elif days <= 90:
        df['periode'] = df['start_date'].dt.to_period('W').apply(lambda r: r.start_time.date())  # par semaine
        x_labels = df['periode'].sort_values().unique()
        #title = "Distance hebdomadaire"
    else:
        df['periode'] = df['start_date'].dt.to_period('M').apply(lambda r: r.start_time.date())  # par mois
        x_labels = df['periode'].sort_values().unique()
        #title = "Distance mensuelle"

    # Agrégation des distances (en km)
    grouped = df.groupby('periode')['distance'].sum() / 1000
    y_values = [grouped.get(x, 0) for x in x_labels]
    text_values = [str(round(km)) for km in y_values]


    # Construction du graphique
    figure = go.Figure()
    figure.add_trace(go.Bar(
        name='Distance',
        text=text_values,
        x=[str(x) for x in x_labels],
        y=y_values,
        textposition='outside',
        cliponaxis=False,
        marker=dict(color='#5FB49C', line=dict(color='black', width=0.5)),
        textfont=dict(color='white', family='monospace', size=15),
        opacity=0.85
    ))

    # Layout du graphique
    figure.update_layout(
        #title=title,
        barcornerradius=5,
        uirevision=False,
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='white',
            tickangle=0,
            tickfont=dict(color='white', family='monospace'),
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
        margin=dict(t=30, b=30, l=30, r=30),
    )

    return figure
