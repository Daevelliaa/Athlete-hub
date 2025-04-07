import plotly.graph_objects as go
import pandas as pd

def scatter_pr(df):
    df = df.copy()
    df['start_date'] = pd.to_datetime(df['start_date'])

    # Calcul de la période
    start = df['start_date'].min()
    end = df['start_date'].max()
    days = (end - start).days

    # Agrégation dynamique
    if days <= 14:
        df['periode'] = df['start_date'].dt.date
        #title = "PR par jour"
    elif days <= 90:
        df['periode'] = df['start_date'].dt.to_period('W').apply(lambda r: r.start_time.date())
        #title = "PR par semaine"
    else:
        df['periode'] = df['start_date'].dt.to_period('M').apply(lambda r: r.start_time.date())
        #title = "PR par mois"

    grouped = df.groupby('periode')['pr_count'].sum().fillna(0)
    x_labels = grouped.index.astype(str).tolist()
    y_values = grouped.values.tolist()

    # Création du graphique
    figure = go.Figure()

    figure.add_trace(
        go.Scatter(
            x=x_labels,
            y=y_values,
            mode="lines+markers+text",
            text=y_values,
            textposition='top center',
            textfont=dict(
                color='white',
                size=10  
            ),
            line=dict(
                shape='hvh',
                width=2,
                color='#5FB49C',
            ),
            marker=dict(
                size=6,
                color='white',
            )
        )
    )

    figure.update_layout(
        #title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            tickangle=0,
            tickfont=dict(
                color="white",
                family='monospace',
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
        font=dict(color="white"),
        margin=dict(t=30, b=30, l=30, r=30),
    )

    return figure
