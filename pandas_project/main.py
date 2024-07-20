import pandas as pd
import re
from collections import Counter

df = pd.read_csv('data\django_crypto_twitter_influencers_tweet.csv',low_memory=False)

def sort(pattern,x) :
    def find_words(text):
        return re.findall(pattern, str(text))
    words = df['full_text'].apply(find_words).explode().dropna().tolist()
    counter = Counter(words)
    sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    indexed_list = [(index + 1, dollar_word, count) for index, (dollar_word, count) in enumerate(sorted_list)]
    sorted_df = pd.DataFrame(indexed_list, columns=['Index', 'Name', 'Count'])
    sorted_df.to_csv(x, index=False)

hashtag_pattern = r'#(\w+)'
mention_pattern = r'@(\w+)'
dollar_pattern = r'\$(\w+)'

sort(hashtag_pattern,x='sorted_hashtags.csv')
sort(mention_pattern,x='sorted_mentions.csv')
sort(dollar_pattern,x='sorted_dollars.csv')