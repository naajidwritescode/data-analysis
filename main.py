import pandas as pd
import numpy as np

# Load the data set
df = pd.read_csv('netflix_titles.csv')

# View data information
print("\nFirst Five rows:\n")
print(df.head())

print("\nData Information\n")
print(df.info)
print("\nData Description:\n")
print(df.describe())

print(df.columns)


# Cleaning missing data
print(df.isnull().sum())

df['director'] = df['director'].fillna('unknown')
df['cast'] = df['cast'].fillna('not available')
df['country'] = df['country'].fillna(
    df['country'].mode()[0])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df = df.dropna(subset=['duration', 'date_added'])

print(df.isnull().sum())


# Movie vs TV Show

most_type = df['type'].value_counts()
print()
print(f"Total Movies: {most_type['Movie']}")
print(f"Total TV shows: {most_type['TV Show']}")
print()


# Top Genre
top_genres = df['listed_in'].str.split(', ').explode()
top_genre = top_genres.value_counts()
print("\nTop 3 genres are:")
print(top_genre.index[0])  # Top 1 genre name
print(top_genre.index[1])  # Top 2 genre name
print(top_genre.index[2])  # Top 3 genre name
print()


# Top Country
top_courty = df['country'].value_counts()
print('\nTop 3 contries producing most content:\n')
print(top_courty.index[0])
print(top_courty.index[1])
print(top_courty.index[2])
print()


# Trend over time
trend = df['release_year'].value_counts()
print("\nTop 3 years releasing most shows\n")
print(trend.index[0])
print(trend.index[1])
print(trend.index[2])
print()


# Top Directors
directors_split = df['director'].str.split(', ').explode()
directors_split = directors_split[directors_split != 'unknown']
director = directors_split.value_counts()
print("\nTop 3 directors:\n")
print(director.index[0])
print(director.index[1])
print(director.index[2])
print()


# Average duration of movies
movie = df[df['type'] == 'Movie']

movie_duration = movie['duration'].str.extract('(\d+)').astype(float)
movie_array = np.array(movie_duration)
avg_movie_length = movie_array.mean()
print(f"Average movie duration is {round(avg_movie_length)} minutes")


# Average duration of TV shows
TV_show = df[df['type'] == 'TV Show']

show_duration = TV_show['duration'].str.extract('(\d+)').astype(int)
show_array = np.array(show_duration)
avg_show_length = show_array.mean()
print(f"Average show duration is {round(avg_show_length)} seasons")


# Saving the cleaned data_set

df.to_csv('cleaned_netflix_data.csv')
