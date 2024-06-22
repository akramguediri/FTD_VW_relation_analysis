from textblob import TextBlob
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Load articles
with open('../data/news_articles.json', 'r') as f:
    articles = json.load(f)

# Extract sentiment
sentiments = []
for article in articles['articles']:
    text = article['content']
    sentiment = TextBlob(text).sentiment.polarity
    date = article['publishedAt'][:10]
    sentiments.append({'Date': date, 'Sentiment': sentiment})

sentiment_df = pd.DataFrame(sentiments)
sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date'])
sentiment_df.set_index('Date', inplace=True)

# Plot sentiment over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=sentiment_df, x='Date', y='Sentiment')
plt.title('News Sentiment Over Time')
plt.show()
