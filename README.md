# Bundesliga_Relationship_GoaldifferentialAndRank
Within this project the relationship between the goal differential and the rank in the Bundesliga table at the end of the season is analyzed. This analysis helps to analyze if a team overperformed or underperformed during a season. It helps to understand the relationship between goal differental and rank in Deutsche Fußball Bundesliga and can help to classify the performance of a team better than by only looking to the rank. This could be especially important in a sports like football in which coincidence plays a crucial role.

## Data Collection and Understanding
The data is scraped from http://bulibox.de/abschlusstabellen/index.html. To scrape the data BeautifulSoup was used. The data was collected since the existence of the Bundesliga (1963/64 until 2020/21). To understand the data the correlation between the numeric columns was calculated. It becomes obvious that there are strong correlations between some variables (goal differential and rank, points and goals etc.)
![image](https://user-images.githubusercontent.com/66475927/155399371-51222760-ed4b-497a-8e55-9f4981ab53b5.png)

Furthermore it was analyzed how often the teams won the Deutsche Meisterschaft in Bundesliga. Bayern München is the team with the most wins.
![image](https://user-images.githubusercontent.com/66475927/155399772-803da7a3-ec6e-4fee-9d65-253db51c60d4.png)

## Data Preparation
One season in Deutsche Bundesliga was played with 20 teams after Western and Eastern Germany got reunited. This season was excluded from the analysis in order to have only consistent numbers of teams (18 teams per season).

## Model Building and Conclusion
Afterwards a linear regression model was built. R2 score of the model is 0,80. Root mean squared error and mean absolute error are also in an acceptable range.

![image](https://user-images.githubusercontent.com/66475927/155403428-81f3d57f-d73f-4edf-93a5-c224d5407ef8.png)

In the illustration it is visible that there is a strong relationship between goal differential and the rank. The more positive the goal differential the better is the rank and the more negative the worse is the rank of a team at the end of a season.
