# Netflix Data Analysis

## Overview
This project analyzes a Netflix dataset to uncover insights about content types, genres, countries of production, release trends, and durations of movies and TV shows. It demonstrates data cleaning, exploration, and visualization using Python libraries **Pandas**, **NumPy**, and **Matplotlib**.

---

## Dataset
- The dataset used is `netflix_titles.csv`.
- It contains metadata about Netflix movies and TV shows including title, director, cast, country, release year, duration, genres, and ratings.

---

## Key Features

### Data Cleaning
- Removed duplicate records.
- Handled missing values:
  - Filled missing `director` and `cast` with `"unknown"` or `"not available"`.
  - Imputed missing `country` and `rating` with the mode (most common value).
  - Dropped rows missing critical `duration` or `date_added` values.

### Data Exploration & Visualizations
- **Movie vs TV Show distribution:** Pie chart showing the proportion of movies and TV shows.
- **Top genres:** Bar chart of the three most frequent genres.
- **Top countries producing Netflix content:** Bar chart of top 3 countries.
- **Content release trend over time:** Line chart showing number of shows released per year.
- **Top directors:** Bar chart of the three most prolific directors.
- **Average duration:** Calculated average movie length in minutes and average TV show length in seasons.

