import pandas as pd
import re
from collections import Counter

df = pd.read_csv('data\django_crypto_twitter_influencers_tweet.csv',low_memory=False)
hashtag_pattern = r'#(\w+)'
def find_hashtags(text):
    return re.findall(hashtag_pattern, str(text))
hashtags = df['full_text'].apply(find_hashtags).explode().dropna().tolist()
hashtag_counter = Counter(hashtags)
sorted_hashtags = sorted(hashtag_counter.items(), key=lambda x: x[1], reverse=True)
indexed_hashtags = [(index + 1, hashtag, count) for index, (hashtag, count) in enumerate(sorted_hashtags)]
sorted_hashtags_df = pd.DataFrame(indexed_hashtags, columns=['Index', 'Name', 'Count'])
sorted_hashtags_df.to_csv('sorted_hashtags.csv', index=False)

print("The sorted hashtag counts have been saved to 'sorted_hashtags.csv'")


mention_pattern = r'@(\w+)'
def find_mentions(text):
    return re.findall(mention_pattern, str(text))
mentions = df['full_text'].apply(find_mentions).explode().dropna().tolist()
mention_counter = Counter(mentions)
sorted_mentions = sorted(mention_counter.items(), key=lambda x: x[1], reverse=True)
indexed_mentions = [(index + 1, mention, count) for index, (mention, count) in enumerate(sorted_mentions)]
sorted_mentions_df = pd.DataFrame(indexed_mentions, columns=['Index', 'Name', 'Count'])
sorted_mentions_df.to_csv('sorted_mentions.csv', index=False)

print("The sorted mention counts have been saved to 'sorted_mentions.csv'")


dollar_pattern = r'\$(\w+)'
def find_dollar_words(text):
    return re.findall(dollar_pattern, str(text))
dollar_words = df['full_text'].apply(find_dollar_words).explode().dropna().tolist()
dollar_counter = Counter(dollar_words)
sorted_dollars = sorted(dollar_counter.items(), key=lambda x: x[1], reverse=True)
indexed_dollars = [(index + 1, dollar_word, count) for index, (dollar_word, count) in enumerate(sorted_dollars)]
sorted_dollars_df = pd.DataFrame(indexed_dollars, columns=['Index', 'Name', 'Count'])
sorted_dollars_df.to_csv('sorted_dollars.csv', index=False)

print("The sorted dollar word counts have been saved to 'sorted_dollars.csv'")
