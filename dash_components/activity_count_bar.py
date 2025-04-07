import plotly.graph_objs as go
import pandas as pd

def activity_count_bar(df):
    df = df.copy()
    df['start_date'] = pd.to_datetime(df['start_date'])

    # 🧠 Déterminer la durée de la période
    start = df['start_date'].min()
    end = df['start_date'].max()
    days = (end - start).days

    # ⏱️ Choisir la fréquence
    if days <= 14:
        df['periode'] = df['start_date'].dt.date
        #title = "Nombre d'activités par jour"
    elif days <= 90:
        df['periode'] = df['start_date'].dt.to_period('W').apply(lambda r: r.start_time.date())
        #title = "Nombre d'activités par semaine"
    else:
        df['periode'] = df['start_date'].dt.to_period('M').apply(lambda r: r.start_time.date())
        #title = "Nombre d'activités par mois"

    # 📊 Comptage des activités
    grouped = df.groupby('periode').size()
    x_labels = grouped.index.astype(str).tolist()
    y_values = grouped.values.tolist()
    text_values = [str(v) for v in y_values]

    # 📈 Construction du graphique
    fig = go.Figure(data=[
        go.Bar(
            x=x_labels,
            y=y_values,
            text=text_values,
            textposition='outside',
            marker=dict(color='#5FB49C', line=dict(color='black', width=0.5)),
            textfont=dict(color='white', size=13, family='monospace'),
            opacity=0.85
        )
    ])

    fig.update_layout(
        #title=title,
        barcornerradius=5,
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
        uniformtext=dict(
            minsize=14,
            mode='show'  # ou 'hide' si tu veux éviter les chevauchements
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        showlegend=False,
        margin=dict(t=30, b=30, l=30, r=30),
    )

    return fig
