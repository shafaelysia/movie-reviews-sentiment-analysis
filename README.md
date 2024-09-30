# Movie Reviews Sentiment Analysis
## Project Overview
This project utilizes Natural Language Processing (NLP) to analyze sentiments from movie reviews.
The goal is to understand how viewers feel about movies by classifying reviews into three categories:
**positive** and **negative** sentiments.
## Web App

## Data Collection
The dataset consists of reviews for 20 movies scraped from **IMDb**, with each movie having its 100 most voted reviews.
These 20 movies include a combination of 10 classic films and 10 recent releases (2022-2023). The scraping process was
performed using Selenium, and all reviews were preprocessed to remove any unnecessary text before conducting
sentiment analysis.
## Sentiment Analysis Method
The reviews sentiments are classifies using [siebert/sentiment-roberta-large-english](https://huggingface.co/siebert/sentiment-roberta-large-english)
from Hugging Face, a state-of-the-art transformer model that accurately classifies reviews into positive or negative sentiments.