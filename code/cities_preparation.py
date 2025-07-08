import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# open and read .csv file
df = pd.read_csv('/Users/stucco/Desktop/data analysis/actionable projects/project_2_cities/travel_cities_cleaned.csv')

# group columns with ratings
rating_cols = [
    'adventure', 'beaches', 'cuisine', 'culture', 'nature', 'nightlife', 'seclusion', 'urban', 'wellness'
]

# assign values to budget types
budget_remap = {'Budget' : 3, 'Mid-range': 2, 'Luxury' : 1}

# assign arbitrary grades to average yearly temperatures
df['avg_temp_year'] = df[[f'avg_temp_month_{m}' for m in range(1, 13)]].mean(axis = 1).round(3)
def temp_rating(temp):
    if 20 <= temp <= 22:
        return 10
    elif 19 <= temp < 20 or 22 < temp <= 23:
        return 9
    elif 18 <= temp < 19 or 23 < temp <= 24:
        return 8
    elif 16 <= temp < 18:
        return 7
    elif 14 <= temp < 16 or 24 < temp <= 25:
        return 6
    elif 12 <= temp < 14 or 25 < temp <= 26:
        return 5
    elif 10 <= temp < 12 or 26 < temp <= 27:
        return 4
    elif 8 <= temp < 10 or 27 < temp <= 28:
        return 3
    elif 5 <= temp < 8 or 28 < temp <= 29:
        return 2
    else:  # temp <5 or >29
        return 1

# define the 3 categories to carry out PCA on
df['ratings_score'] = df[rating_cols].mean(axis = 1).round(3)
df['budget_score'] = df['budget_level'].map(budget_remap)
df['climate_score'] = df['avg_temp_year'].apply(temp_rating)

pca_features = df[['ratings_score', 'budget_score', 'climate_score']]

# scale PCA features so that their weight is equal
scaler = StandardScaler()
pca_features_scaled = scaler.fit_transform(pca_features)

# run PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(pca_features_scaled)

# prepare PCA results
df['pca_1'] = pca_result[:, 0]
df['pca_2'] = pca_result[:, 1]

# formula for combined PCAs
df['pca_score'] = df['pca_2'] - df['pca_1']

# add global ranking column
df['global_rank'] = df['pca_score'].rank(method='dense', ascending=False).astype(int)

# add country-specific ranking column
df['country_rank'] = df.groupby('country')['pca_score'].rank(method='dense', ascending=False).astype(int)

# convert latitude and longitude columns to numeric and round to 7
# due to messed up CSV reading in Tableau
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce').round(7)
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce').round(7)

# set final dataset structure
city_description = df[['id', 'city', 'country', 'region', 'short_description', 'latitude',
                       'longitude', 'ideal_durations', 'avg_temp_year', 'budget_level',
                       'ratings_score', 'budget_score', 'climate_score', 'pca_score']]

city_temperatures = df[['id', 'avg_temp_month_1', 'avg_temp_month_2', 'avg_temp_month_3',
                        'avg_temp_month_4', 'avg_temp_month_5', 'avg_temp_month_6',
                        'avg_temp_month_7', 'avg_temp_month_8', 'avg_temp_month_9',
                        'avg_temp_month_10', 'avg_temp_month_11', 'avg_temp_month_12']]

city_ratings = df[['id', 'adventure', 'beaches', 'cuisine', 'culture', 'nature', 'nightlife', 'seclusion', 'urban', 'wellness']]

city_ranking = df[['id', 'global_rank', 'country_rank']]

# save CSV files
city_description.to_csv('city_description.csv', index=False)
city_temperatures.to_csv('city_temperatures.csv', index=False)
city_ratings.to_csv('city_ratings.csv', index=False)
city_ranking.to_csv('city_ranking.csv', index=False)
