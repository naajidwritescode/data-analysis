import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

# Drop Duplicates
df = df.drop_duplicates()

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
plt.figure()
plt.pie([most_type['Movie'], most_type['TV Show']],
        labels=['Movie', 'TV Show'], autopct='%1.1f%%')
plt.title('Movie vs TV show')
plt.legend()
plt.tight_layout()
plt.savefig('movies_vs_tvshow.png', dpi=300, bbox_inches='tight')

# Top Genre

top_genres = df['listed_in'].str.split(', ').explode()
top_genre = top_genres.value_counts()
print("\nTop 3 genres are:")
print(top_genre.index[0])  # Top 1 genre name
print(top_genre.index[1])  # Top 2 genre name
print(top_genre.index[2])  # Top 3 genre name
print()

plt.figure()
plt.bar([top_genre.index[0], top_genre.index[1], top_genre.index[2]], [
        top_genre.iloc[0], top_genre.iloc[1], top_genre.iloc[2]], label='Top Genre', color='red')
plt.title("Top 3 Genre")
plt.legend()
plt.xlabel('Genre')
plt.ylabel('Number of shows')
plt.grid(color='grey', linestyle='-', linewidth='0.3')
plt.tight_layout()
plt.savefig('top_genre.png', dpi=300, bbox_inches='tight')

# Top Country
top_country = df['country'].value_counts()
print('\nTop 3 contries producing most content:\n')
print(top_country.index[0])
print(top_country.index[1])
print(top_country.index[2])
print()
plt.figure()
plt.bar([top_country.index[0], top_country.index[1], top_country.index[2]], [
        top_country.iloc[0], top_country.iloc[1], top_country.iloc[2]], label='Top Country', color='purple')
plt.title("Top 3 Countries")
plt.xlabel('Countries')
plt.ylabel('Number of Shows')
plt.legend()
plt.grid(color='grey', linestyle='-', linewidth='0.3')
plt.tight_layout()
plt.savefig('top_country.png', dpi=300, bbox_inches='tight')

# Trend over time
trend = df['release_year'].value_counts()
print("\nTop 3 years releasing most shows\n")
print("\nTop 3 years releasing most shows\n")
print(f"{trend.index[0]}: {trend.iloc[0]} shows")
print(f"{trend.index[1]}: {trend.iloc[1]} shows")
print(f"{trend.index[2]}: {trend.iloc[2]} shows\n")

trend_sorted = df['release_year'].value_counts().sort_index()

plt.figure()
plt.plot(trend_sorted.index, trend_sorted.values, color='orange', marker='o')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.title('Number of Shows Released per Year')
plt.grid()
plt.tight_layout()
plt.savefig('shows_per_year.png', dpi=300, bbox_inches='tight')

# Top Directors
directors_split = df['director'].str.split(', ').explode()
directors_split = directors_split[directors_split != 'unknown']
director = directors_split.value_counts()
print("\nTop 3 Directors:\n")
print(director.index[0])
print(director.index[1])
print(director.index[2])
print()
plt.figure()
plt.bar([director.index[0], director.index[1], director.index[2]], [
        director.iloc[0], director.iloc[1], director.iloc[2]], label='Top Dirctors', color='steelblue')
plt.title("Top 3 Directors")
plt.legend()
plt.xlabel('Directors')
plt.ylabel('Number of Shows')
plt.grid(color='grey', linestyle='-', linewidth='0.3')
plt.savefig('top_directors.png', dpi=300, bbox_inches='tight')

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
