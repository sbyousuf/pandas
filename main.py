import pandas as pd

df=pd.read_csv('django_crypto_twitter_influencers_tweet.csv' ,low_memory=False)
df1=df['full_text']
# Step 2: Replace NaN values with empty strings
df2 = df1.fillna('')
hashtag=0
cnt_addesign=0
cnt_dollar=0
for i in df2:
    if "#" in i:
        hashtag+=1
    if "$" in i:
        cnt_dollar+=1
    if "@" in i :
        cnt_addesign+=1

print(f"@:{cnt_addesign}")
print(f"#:{hashtag}")
print(f"$:{cnt_dollar}")


