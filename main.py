import pandas as pd
import re
from collections import Counter

# Read the CSV file
df = pd.read_csv('django_crypto_twitter_influencers_tweet.csv',low_memory=False)

# Define a regex pattern to find hashtags
hashtag_pattern = r'#(\w+)'

# Function to find hashtags in a text
def find_hashtags(text):
    return re.findall(hashtag_pattern, str(text))

# Apply the function to the "full text" column and flatten the list
hashtags = df['full_text'].apply(find_hashtags).explode().dropna().tolist()

# Count occurrences of each hashtag
hashtag_counter = Counter(hashtags)

# Convert the counter to a sorted list of tuples (index, hashtag, count)
sorted_hashtags = sorted(hashtag_counter.items(), key=lambda x: x[1], reverse=True)
indexed_hashtags = [(index + 1, hashtag, count) for index, (hashtag, count) in enumerate(sorted_hashtags)]

# Create a DataFrame from the sorted list
sorted_hashtags_df = pd.DataFrame(indexed_hashtags, columns=['Index', 'Name', 'Count'])

# Write the DataFrame to a new CSV file
sorted_hashtags_df.to_csv('sorted_hashtags.csv', index=False)

print("The sorted hashtag counts have been saved to 'sorted_hashtags.csv'")
