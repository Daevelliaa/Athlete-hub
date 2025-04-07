import plotly.graph_objects as go
import pandas as pd

def distance_range_donut(df):
    df = df.copy()
    df['distance_km'] = df['distance'] / 1000

    # 🎯 Définir les bins
    bins = [0, 20, 40, 70, 100, float('inf')]
    labels = ['1–20', '21–40', '41–70', '71–100', '100+']

    # 📊 Regrouper les activités par range
    df['range'] = pd.cut(df['distance_km'], bins=bins, labels=labels, right=True)
    range_counts = df['range'].value_counts().reindex(labels, fill_value=0)

    # 📈 Création du donut chart
    fig = go.Figure(data=[go.Pie(
        labels=range_counts.index.tolist(),
        values=range_counts.values.tolist(),
        hole=0.6,
        marker=dict(
            colors=['#5FB49C', '#3EC8E3', '#1876A5', '#136BA1', '#0C4A6E'],  # couleur par range
            line=dict(color='white', width=1.5)
        ),
        textinfo='value',
        textposition='inside',
        domain=dict(x=[0.2, 0.8], y=[0.1, 0.8]),
        pull=[0.05]*5  # effet stylé qui écarte les parts
    )])

    # 🎨 Mise en forme du layout
    fig.update_layout(
        #title="Distance Ranges",
        title_font_size=20,
        title_font_color='white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            orientation='h',
            x=0.5,
            xanchor='center',
            y=-0.1,
            font=dict(size=14)
        ),
        margin=dict(t=50, b=30, l=30, r=30)
    )

    return fig
