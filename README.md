📊 Netflix Data Analysis Project
This project analyzes the Netflix catalog data using Python and pandas to extract insights on content type, popular genres, trends over the years, average durations, and more. It uses the official netflix_titles.csv dataset from Kaggle.

🔍 Project Overview
This script performs:

Data cleaning (handling missing values)

Analysis of:

Total number of Movies vs. TV Shows

Top genres on the platform

Top countries producing the most content

Release year trends

Top directors with most titles

Average duration of Movies and TV Shows

Exports a cleaned version of the dataset

📁 Files
File Name	Description
main.py	Main script for cleaning and analyzing Netflix data.
netflix_titles.csv	Original dataset from Kaggle containing Netflix catalog details.
cleaned_netflix_data.csv	Cleaned dataset after handling missing values and formatting.
README.md	Documentation of the project.

🧠 Skills Used
Python programming

pandas for data manipulation

numpy for numeric operations

Basic data cleaning and analysis

Data storytelling through print summaries

🧹 Data Cleaning
The script handles missing values by:

Column	Strategy
director	Filled with 'unknown'
cast	Filled with 'not available'
country	Filled with the most frequent country
rating	Filled with the most frequent rating
duration	Dropped rows with missing values
date_added	Dropped rows with missing values

📊 Key Insights
Total Movies vs TV Shows on Netflix

Top 3 Genres listed in the catalog

Top 3 Countries with most Netflix content

Top 3 Release Years with highest content production

Top 3 Directors with the most shows or movies

Average Movie Duration in minutes

Average TV Show Duration in seasons

📚 Dataset Source:
Netflix Titles Dataset on Kaggle

👨‍💻 Author:
Naajid Monowar Hossain
