import plotly.graph_objects as go
import pandas as pd

def radar_hr_zones(df):
    df = df.copy()
    df = df[df['average_heartrate'].notnull()]

    # Définir les zones (à adapter selon ton profil !)
    def get_zone(hr):
        if hr < 130: return 'Zone 1'
        elif hr < 142: return 'Zone 2'
        elif hr < 165: return 'Zone 3'
        elif hr < 180: return 'Zone 4'
        else: return 'Zone 5'

    df['zone'] = df['average_heartrate'].apply(get_zone)
    df['moving_time_hours'] = df['moving_time'] / 3600

    # Agréger par sport + zone
    grouped = df.groupby(['type', 'zone'])['moving_time_hours'].sum().unstack(fill_value=0)

    zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

    fig = go.Figure()

    # Tracer une courbe par sport
    for sport in grouped.index:
        values = [grouped.loc[sport].get(zone, 0) for zone in zones]
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=zones,
            fill='toself',
            name=sport,
        ))

    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',  # ← fond du radar noir transparent
            radialaxis=dict(
                visible=True,
                gridcolor='rgba(255,255,255,0.2)',  # lignes fines
                linecolor='white',
                tickfont=dict(color='white'),
                tickangle=0,
            ),
            angularaxis=dict(
                tickfont=dict(color='white'),
                gridcolor='rgba(255,255,255,0.2)',  # lignes rayons
                linecolor='white'
            )
        ),
        paper_bgcolor='rgba(0,0,0,0)',  # ← fond général
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            orientation='h',
            x=0.5, xanchor='center', y=-0.2,
            font=dict(size=14)
        ),
        margin=dict(t=50, b=50, l=30, r=30)
    )


    return fig
