'''
Rodolfo Ferreira
Programming for Big Data
Id 10540987
CA4 - Pandas Data Interpretation
github https://github.com/rodbferreira/B8IT105-RF
'''

import pandas as pd


#import dataset
dataset = pd.read_csv("premierleague.csv") #Premier League May - July 2017 data
#https://www.kaggle.com/mauryashubham/english-premier-league-players-dataset

print(dataset)

#examine dataset
dataset.head()
dataset.tail()
dataset.index
dataset.columns
dataset.shape
dataset.info()
dataset.describe()
dataset.dtypes

# Plot Age average per Club
dataset.groupby('club')['age'].mean().plot.bar(x='club', y='age')

#Youngest player in Premier League
dataset.loc[dataset['age'].idxmin()]

# Plot most valuable Club (by pleayers)
dataset.groupby('club')['market_value'].sum().plot.bar(x='club', y='market_value')

#Most Expensive player in Premier League
dataset.loc[dataset['market_value'].idxmax()]

# Plot most fan pages viwes by Club couting all players
dataset.groupby('club')['page_views'].sum().plot.bar(x='club', y='page_views')

#Player with the highest fans pages view
dataset.loc[dataset['page_views'].idxmax()]

# Different Natinalities by Club
dataset.groupby('club')['nationality'].nunique().plot.bar(x='club', y='nationality')

#Count Nationalities in Premier League (sorted By the higher number of Nacionalities)
dataset.nationality.value_counts().head(10)

# Plot Top 10 Count Nationalities in Premier League 
dataset.nationality.value_counts().head(10).plot.pie()




