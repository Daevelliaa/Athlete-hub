import plotly.graph_objs as go
import pandas as pd

def bar_elevation(df):
    df = df.copy()
    df['start_date'] = pd.to_datetime(df['start_date'])

    # Déterminer la durée de la période sélectionnée
    start = df['start_date'].min()
    end = df['start_date'].max()
    days = (end - start).days

    # Choix de l'agrégation (par jour, semaine ou mois)
    if days <= 14:
        df['periode'] = df['start_date'].dt.date
        #title = "Dénivelé quotidien"
    elif days <= 90:
        df['periode'] = df['start_date'].dt.to_period('W').apply(lambda r: r.start_time.date())
        #title = "Dénivelé hebdomadaire"
    else:
        df['periode'] = df['start_date'].dt.to_period('M').apply(lambda r: r.start_time.date())
        #title = "Dénivelé mensuel"

    # Agrégation du dénivelé (en km arrondi)
    grouped = df.groupby('periode')["total_elevation_gain"].sum() 
    grouped = grouped.round().astype(int)

    x_labels = grouped.index.astype(str).tolist()
    y_values = grouped.values.tolist()
    text_values = [str(v) for v in y_values]

    # Création du graphique
    figure = go.Figure(
        data=[go.Bar(
            name='Dénivelé',
            x=x_labels,
            y=y_values,
            text=text_values,
            textposition='outside',
            marker=dict(color='#5FB49C', line=dict(color='black', width=0.5)),
            textfont=dict(
                color='white',
                family='monospace',
                size=15  # texte plus grand
            ),
            opacity=0.85
        )]
    )

    # Mise en forme
    figure.update_layout(
        #title=title,
        barcornerradius=5,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
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
