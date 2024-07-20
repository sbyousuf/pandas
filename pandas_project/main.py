import pandas as pd
import re
from collections import Counter

# Read the CSV file
df = pd.read_csv('data\django_crypto_twitter_influencers_tweet.csv',low_memory=False)

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


# Define a regex pattern to find mentions (@)
mention_pattern = r'@(\w+)'

# Function to find mentions in a text
def find_mentions(text):
    return re.findall(mention_pattern, str(text))

# Apply the function to the "full text" column and flatten the list
mentions = df['full_text'].apply(find_mentions).explode().dropna().tolist()

# Count occurrences of each mention
mention_counter = Counter(mentions)

# Convert the counter to a sorted list of tuples (index, mention, count)
sorted_mentions = sorted(mention_counter.items(), key=lambda x: x[1], reverse=True)
indexed_mentions = [(index + 1, mention, count) for index, (mention, count) in enumerate(sorted_mentions)]

# Create a DataFrame from the sorted list
sorted_mentions_df = pd.DataFrame(indexed_mentions, columns=['Index', 'Name', 'Count'])

# Write the DataFrame to a new CSV file
sorted_mentions_df.to_csv('sorted_mentions.csv', index=False)

print("The sorted mention counts have been saved to 'sorted_mentions.csv'")

# Define a regex pattern to find dollar signs ($) followed by words
dollar_pattern = r'\$(\w+)'

# Function to find dollar sign words in a text
def find_dollar_words(text):
    return re.findall(dollar_pattern, str(text))

# Apply the function to the "full text" column and flatten the list
dollar_words = df['full_text'].apply(find_dollar_words).explode().dropna().tolist()

# Count occurrences of each dollar word
dollar_counter = Counter(dollar_words)

# Convert the counter to a sorted list of tuples (index, dollar word, count)
sorted_dollars = sorted(dollar_counter.items(), key=lambda x: x[1], reverse=True)
indexed_dollars = [(index + 1, dollar_word, count) for index, (dollar_word, count) in enumerate(sorted_dollars)]

# Create a DataFrame from the sorted list
sorted_dollars_df = pd.DataFrame(indexed_dollars, columns=['Index', 'Name', 'Count'])

# Write the DataFrame to a new CSV file
sorted_dollars_df.to_csv('sorted_dollars.csv', index=False)

print("The sorted dollar word counts have been saved to 'sorted_dollars.csv'")
