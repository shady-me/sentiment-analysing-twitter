import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Load the data
df = pd.read_csv('tweets.csv')

# Print the column names to verify
print("Columns in DataFrame:", df.columns)

# Function to clean tweets
def clean_tweet(tweet):
    try:
        tweet = re.sub(r'@\w+', '', tweet)  # Remove mentions
        tweet = re.sub(r'http\S+|www\S+', '', tweet)  # Remove URLs
        tweet = re.sub(r'\W', ' ', tweet)  # Remove special characters
        tweet = tweet.lower()  # Convert to lowercase
        tweet = tweet.split()  # Split into words
        tweet = [word for word in tweet if word not in stopwords.words('english')]  # Remove stopwords
        return ' '.join(tweet)  # Join words back into a single string
    except Exception as e:
        print(f"Error cleaning tweet: {e}")
        return tweet  # Return the original tweet if there's an error

# Clean the tweets
df['cleaned_text'] = df['text'].apply(clean_tweet)

# Print the first few rows of the original and cleaned data
print("Original Tweets:")
print(df['text'].head())
print("Cleaned Tweets:")
print(df['cleaned_text'].head())

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_tweets.csv', index=False)
print("Cleaned tweets saved to cleaned_tweets.csv")