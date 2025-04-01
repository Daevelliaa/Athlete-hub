import json
import pandas as pd
import plotly.express as px

with open("activities_2024.json", 'r', encoding='utf-8') as f:
    data=json.load(f)

df=pd.DataFrame(data)

# Assure-toi que la colonne est bien datetime
df['start_date'] = pd.to_datetime(df['start_date'])

# Optionnel : filtrer uniquement l'année 2024
df_2024 = df[df['start_date'].dt.year == 2024]

# Extraire le mois et on créé une colonne avec les mois 1 à 12
df_2024['month'] = df_2024['start_date'].dt.month

# Grouper par mois et sommer les pr_count
monthly_pr = df_2024.groupby('month')['pr_count'].sum()

# Assure que tous les mois sont présents (même avec 0 PR)
monthly_pr = monthly_pr.reindex(range(1, 13), fill_value=0)

print(monthly_pr)