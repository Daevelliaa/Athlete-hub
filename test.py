import json
import pandas as pd
import plotly.express as px

with open("activities_2024.json", 'r', encoding='utf-8') as f:
    data=json.load(f)

df=pd.DataFrame(data)

# Étape 2 : Grouper par type d’activité et faire la somme
time_by_activity = (df.groupby('type')['moving_time'].sum()/3600).astype(int)

# Optionnel : trier du plus long au plus court
time_by_activity = time_by_activity.sort_values(ascending=False)

print(time_by_activity)