# Where-to-next

<table>
  <tr>
    <td><img src="tableau/overview.jpg" alt="PCA Overview" width="400"/></td>
    <td><img src="tableau/destination_breakdown.jpg" alt="Top & Bottom Cities" width="400"/></td>
  </tr>
</table>

## A Travel Destination Analysis

Choosing where to travel involves trade-offs: How expensive is it? Will the weather be decent? Will I actually enjoy it?

This project uses Principal Component Analysis (PCA) to cut through the noise and mathematically rank over 100 global cities using three essential travel criteria:
	•	Budget – average cost of lodging, food, and transportation
	•	Ratings – traveler satisfaction across attractions, safety, and experience
	•	Climate – average weather conditions, variability, and seasonal comfort

PCA reduces this multi-dimensional data into a simpler form, allowing us to rank cities not just subjectively—but statistically


## Data Overview

### Data Sources

The dataset aggregates public data from a travel review [website](https://www.kaggle.com/datasets/furkanima/worldwide-travel-cities-ratings-and-climate).

### Initial Data Checks

- Missing values were found in climate data for a few cities—these were imputed using regional averages.
- City names were standardized to avoid duplicates due to misspellings.

### Data Cleaning & Formatting

Python scripts were used for data wrangling and PCA transformation.

### Data Structure

The final dataset includes the following fields:
	•	city, country
	•	avg_budget_per_day
	•	avg_rating
	•	climate_score (normalized for temperature range and precipitation)
	•	pca_1, pca_2, pca_score_total

### Data Visualization

Visualizations were created in Tableau Public, accessible here.

### Data Limitations
- No visa/travel restriction data included
- No local event seasonality
- Data reflects average values, not peak/off-peak variance


## Key Questions

This project is structured around three main questions:
	1.	Which cities rank highest overall when budget, ratings, and climate are considered together?
	2.	What characteristics do bottom-ranked cities share?
	3.	Can PCA reveal clusters of similar travel destinations?


## Key Findings

The PCA transformation revealed clear patterns among global travel destinations:
	•	Top 10 Cities:
	•	Destinations like Sydney, Florianópolis, Crete, and Funchal stood out for combining excellent traveler ratings with strong climate scores.
	•	Notably, all top cities had the lowest possible budget score (1–2), meaning they are among the most affordable in the dataset.
	•	Climate and ratings both played a key role: nearly all top cities scored 8 or higher in climate, while holding ratings > 3.6.
	•	Bottom 10 Cities:
	•	Cities such as Naypyidaw, Phnom Penh, Dhaka, and El Chaltén scored low due to poor climate (scores 1–4) and low traveler satisfaction.
	•	Many bottom-ranked cities had the highest budget score (3), signaling low cost, but this wasn’t enough to compensate for unfavorable weather or mediocre reviews.
| Rank | City             |   Score   | Budget        | Climate        | Ratings        |
|------|------------------|-----------|---------------|----------------|----------------|
| 1    | Sydney           | +3.98     | 1             | 8              | 3.89           |
| 2    | Florianópolis    | +3.68     | 2             | 10             | 3.89           |
| 3    | Los Angeles      | +3.66     | 1             | 8              | 3.78           |
| 4    | Crete            | +3.61     | 2             | 8              | 4.11           |
| 5    | Antalya          | +3.32     | 2             | 9              | 3.89           |
| 6    | San Diego        | +3.29     | 2             | 8              | 4.00           |
| 7    | Honolulu         | +3.24     | 1             | 5              | 4.00           |
| 8    | Hamilton         | +3.04     | 1             | 9              | 3.44           |
| 9    | Gold Coast       | +3.03     | 2             | 10             | 3.67           |
| 10   | Funchal          | +3.03     | 2             | 10             | 3.67           |
| -    | -                | -         | -             | -              | -              |
| 551  | Pristina         | –3.34     | 3             | 5              | 2.44           |
| 552  | Yamoussoukro     | –3.37     | 3             | 4              | 2.56           |
| 553  | Chisinau         | –3.37     | 3             | 4              | 2.56           |
| 554  | Astana           | –3.42     | 2             | 1              | 2.56           |
| 555  | Tartu            | –3.43     | 3             | 2              | 2.78           |
| 556  | El Chaltén       | –3.47     | 3             | 1              | 2.89           |
| 557  | Dhaka            | –3.69     | 3             | 4              | 2.44           |
| 558  | Minsk            | –3.72     | 3             | 3              | 2.56           |
| 559  | Phnom Penh       | –4.11     | 3             | 1              | 2.67           |
| 560  | Naypyidaw        | –4.66     | 3             | 4              | 2.11           |

Cost is important—but only when combined with comfort and enjoyment. Cities like Sydney and Crete offer that rare trifecta: affordable, scenic, and highly rated.

Additional insights:
	•	Climate score was a dominant factor in both top and bottom rankings.
	•	All bottom-10 cities had a climate score ≤ 5, while top-10 cities scored ≥ 8.
	•	High ratings alone were not enough if paired with poor weather or high costs.


## Recommendations
- For travelers: Use PCA-style logic—don’t just chase famous destinations. Cities with balance across cost, weather, and ratings offer the most value.
- For tourism boards: Improve climate-friendly infrastructure and value-perception to climb rankings.
- For data nerds: PCA is a powerful tool for reducing complexity. Use it where trade-offs exist across competing variables.

On a microscopic level, travel is deeply personal. But on a macroscopic level, data can highlight which places are objectively better choices for the average traveler.


## Assumptions and Caveats
Climate comfort is based on averages, not personal preference (e.g., some people like winter).
Rating data may be skewed toward English-speaking travelers.
Real-time changes (war, pandemic, political unrest) are not factored in.
