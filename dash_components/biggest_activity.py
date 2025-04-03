import pandas as pd
import plotly.graph_objects as go
import polyline

def biggest_activity_map(df):

    df=df.copy()

    # On vérifie la colonne distance
    if 'distance' not in df or 'map' not in df:
        return go.Figure()
    
    #ici biggest est une ligne complète du dataframe qui est la ligne ou la distance a été la plus grande 
    biggest = df.loc[df['distance'].idxmax()]

    # Décoder la summary_polyline si elle existe
    if 'summary_polyline' in biggest['map']:
        #coords correspond à toutes les coordonnées de la sortie en latitude et longitude
        coords = polyline.decode(biggest['map']['summary_polyline'])
    else:
        return go.Figure()  # Pas de trace dispo, on renvoie une figure vide
    
    # On sépare en lat et lon
    lats, lons = zip(*coords)

    figure = go.Figure()

    figure.add_trace(go.Scattermapbox(
        mode="lines",
        lon=lons,
        lat=lats,
        line=dict(width=4, color='#FFA500'),
        hoverinfo='none',
        ))
    

    figure.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=sum(lats)/len(lats), lon=sum(lons)/len(lons)),
            zoom=8,
        ),
        margin=dict(t=20, b=20, l=40, r=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    return figure

   
