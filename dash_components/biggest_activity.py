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

    polyline_data = biggest.get('map', {}).get('summary_polyline', '')

    # ✅ Nouveau check : polyline présente ET non vide
    if not polyline_data:
        return go.Figure()

    try:
        coords = polyline.decode(polyline_data)
        if not coords:
            return go.Figure()  # la polyline a été décodée mais elle est vide
    except Exception:
        return go.Figure()  # en cas d'erreur de décodage

    # Si tout est bon, on continue
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

   
