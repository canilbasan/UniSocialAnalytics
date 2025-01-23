University Analysis Project

Project Description

This project aims to develop a system that analyzes and ranks universities based on social media comments. By considering criteria such as student satisfaction, social media performance,
and student-friendliness, each university is assigned a score out of 100.
Note: This project focuses solely on universities located in Türkiye.

Features

Sentiment analysis of social media comments
Calculation of positive and negative percentages
Filtering out neutral comments
Scoring and ranking universities
Visual analysis with pie charts
Presentation of data via a Flask-based web application

Technologies Used

Python 3.10.1: Main programming language of the project
Pandas: For data processing and analysis
Matplotlib: For creating visualizations
Flask: For web application development
NLTK/BERT: For natural language processing and sentiment analysis


Clone this repository to your local machine:
git clone https://github.com/canilbasan/UniSocialAnalytics.git
Run the Flask application:
python app.py
Open your browser and navigate to http://127.0.0.1:5000 to explore the application.


Dataset

The project is based on the filtered_percentages.csv file, which includes university names, positive percentages, and negative percentages.


Functionality

Search for university names to view specific sentiment analysis results.
Explore the "Top 10 Universities" tab to see the leading universities.

