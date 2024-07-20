# main.py

from pandas_project.sort_function import sort

# Define patterns for hashtags, mentions, and dollar words
hashtag_pattern = r'#(\w+)'
mention_pattern = r'@(\w+)'
dollar_pattern = r'\$(\w+)'

# Input CSV file path
input_file = 'data/django_crypto_twitter_influencers_tweet.csv'

# Sort and save data for hashtags, mentions, and dollar words
sort(hashtag_pattern, input_file, 'sorted_hashtags.csv')
sort(mention_pattern, input_file, 'sorted_mentions.csv')
sort(dollar_pattern, input_file, 'sorted_dollars.csv')
