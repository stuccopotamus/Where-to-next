import json
import pandas as pd

# import and read csv file
df = pd.read_csv('Worldwide Travel Cities Dataset (Ratings and Climate).csv')

# serialize json values for 'ideal_durations'
df['ideal_durations'] = df['ideal_durations'].apply(json.loads)

# serialize json values, extract averages and create new data columns for 'avg_temp_monthly'
df['avg_temp_monthly_ser'] = df['avg_temp_monthly'].apply(json.loads)

for month in range(1,13):
    month_n = str(month)
    df[f'avg_temp_month_{month_n}'] = df['avg_temp_monthly_ser'].apply(lambda x: x[month_n]['avg'])

# clean useless columns
df_cleaned = df.drop(columns = ['avg_temp_monthly_ser', 'avg_temp_monthly'])

# save new file
df_cleaned.to_csv('travel_cities_cleaned', index=False)
