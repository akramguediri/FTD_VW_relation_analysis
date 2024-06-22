import yfinance as yf
import requests
import json
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Download Volkswagen stock prices
vw_stock = yf.download("VOW.DE", start="2007-01-01", end="2009-01-01")
vw_stock.to_csv('data/volkswagen_stock_prices.csv')

# Download S&P 500 index data
sp500 = yf.download("^GSPC", start="2007-01-01", end="2009-01-01")
sp500.to_csv('data/sp500_index.csv')

# News API parameters
api_key = 'your_api_key'
query = 'Volkswagen'
from_date = '2007-01-01'
to_date = '2009-01-01'

# Fetch news articles
url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&apiKey={api_key}'
response = requests.get(url)
articles = response.json()

# Save news articles to a file
with open('data/news_articles.json', 'w') as f:
    json.dump(articles, f)

print("Data downloaded successfully.")
