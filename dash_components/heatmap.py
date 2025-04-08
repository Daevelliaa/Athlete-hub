# heatmap_utils.py
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import calendar

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

    matrix = np.flipud(matrix)  # Lundi en haut, dimanche en bas
    return matrix

def create_heatmap_figure_from_matrix(matrix, year):
    tickvals, ticktext = [], []
    for m in range(1, 13):
        first_day = datetime(year, m, 1)
        week_idx = first_day.isocalendar()[1] - 1
        if m == 1 and week_idx > 50:
            week_idx = 0
        tickvals.append(week_idx + 1)
        ticktext.append(calendar.month_abbr[m])
        

    fig = go.Figure(data=go.Heatmap(
        z=matrix,
        colorscale=['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353'],
        hoverongaps=True,
        showscale=False,
        xgap=4,
        ygap=4
    ))

    fig.update_layout(
        
        yaxis=dict(showgrid=False, showline=False, zeroline=False, showticklabels=False),
        margin=dict(t=110, b=200, l=5, r=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        #title=f"Heatmap des heures d'activité - {year}"
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
