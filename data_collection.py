import requests
import pandas as pd
import time

# Twitter API credentials
BEARER_TOKEN = 'xxxxxxxB'  # Replace with your actual Bearer Token

# Function to create headers for the request
def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

# Function to fetch tweets using Twitter API v2
def fetch_tweets(query, max_results=100):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields=id,text,created_at&max_results={max_results}"
    headers = create_headers(BEARER_TOKEN)
    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        print("Rate limit exceeded. Waiting for 15 minutes...")
        time.sleep(15 * 60)  # Wait for 15 minutes
        return fetch_tweets(query, max_results)  # Retry the request
    elif response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")

    return response.json()

# Fetch tweets about a specific topic
query = 'YOUR_TOPIC'  # Replace 'YOUR_TOPIC' with your search term
tweets_data = fetch_tweets(query, max_results=100)

# Extract relevant fields and save to DataFrame
tweets = [{'text': tweet.get('text'), 'created_at': tweet.get('created_at')} for tweet in tweets_data.get('data', [])]
df = pd.DataFrame(tweets)

# Save to CSV
df.to_csv('tweets.csv', index=False)
print("Tweets saved to tweets.csv")