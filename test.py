import pandas as pd
import numpy as np
import plotly.graph_objects as go
import calendar
from datetime import datetime
import os

def create_heatmap_matrix_from_df(df, year):
    df['start_date'] = pd.to_datetime(df['start_date'])
    df = df[df['start_date'].dt.year == year]

    df['day'] = df['start_date'].dt.date
    df_grouped = df.groupby('day')['moving_time'].sum().reset_index()
    df_grouped['hours'] = df_grouped['moving_time'] / 3600
    df_grouped = df_grouped[['day', 'hours']]
    df_grouped.columns = ['date', 'hours']

    all_days = pd.date_range(start=f"{year}-01-01", end=f"{year}-12-31")
    df_grouped = df_grouped.set_index('date').reindex(all_days, fill_value=0).reset_index()
    df_grouped.columns = ['date', 'hours']

    df_grouped['weekday'] = df_grouped['date'].dt.weekday
    df_grouped['week'] = df_grouped['date'].dt.isocalendar().week
    df_grouped.loc[(df_grouped['date'].dt.month == 12) & (df_grouped['week'] == 1), 'week'] = 53

    matrix = np.full((7, 53), None)
    for _, row in df_grouped.iterrows():
        week = row['week'] - 1
        day = row['weekday']
        matrix[day, week] = row['hours']
    
    matrix = np.flipud(matrix)  # ← 🧠 retourne les lignes (dimanche en bas, lundi en haut)
    return matrix

def create_heatmap_figure_from_matrix(matrix, year):
    month_lines = []
    tickvals, ticktext = [], []
    for m in range(1, 13):
        first_day = datetime(year, m, 1)
        week_idx = first_day.isocalendar()[1] - 1
        if m == 1 and week_idx > 50:
            week_idx = 0
        tickvals.append(week_idx + 1)
        ticktext.append(calendar.month_abbr[m])
        if m < 12:
            month_lines.append(dict(
                type="line", x0=week_idx + 0.5, x1=week_idx + 0.5,
                y0=-0.5, y1=6.5, line=dict(width=2, color="white")
            ))

    fig = go.Figure(data=go.Heatmap(
        z=matrix,
        colorscale=['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353'],
        hoverongaps=True,
        showscale=False,
        xgap=4,
        ygap=4
    ))

    fig.update_layout(
        shapes=month_lines,
        yaxis=dict(showgrid=False, showline=False, zeroline=False, showticklabels=False),
        margin=dict(t=100, b=100, l=5, r=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=f"Heatmap des heures d'activité - {year}"
    )

    fig.update_xaxes(
        side="top",
        tickmode="array",
        tickvals=tickvals,
        ticktext=ticktext,
        tickfont=dict(color="white", size=12),
        showline=False,
        showgrid=False,
        zeroline=False
    )

    return fig

# ==============================
# 🔽 Lancement du script ici 🔽
# ==============================
if __name__ == "__main__":
    year = 2024
    json_path = "activities_2024.json"

    if not os.path.exists(json_path):
        print(f"❌ Fichier {json_path} introuvable.")
    else:
        print(f"✅ Lecture de {json_path} pour l'année {year}...")
        df = pd.read_json(json_path)
        matrix = create_heatmap_matrix_from_df(df, year)
        fig = create_heatmap_figure_from_matrix(matrix, year)
        fig.show()
