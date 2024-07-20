from pandas_project.sort_function import sort
from pandas_project.plotter import plot_top_words


def main():
    # Load data
    df = "data/django_crypto_twitter_influencers_tweet.csv"

    # Define patterns
    hashtag_pattern = r"#(\w+)"
    mention_pattern = r"@(\w+)"
    dollar_pattern = r"\$(?!\d)\w+"

    # Process data and save to CSV
    hashtags_df = sort(hashtag_pattern, df, "sorted_hashtags.csv")
    mentions_df = sort(mention_pattern, df, "sorted_mentions.csv")
    dollars_df = sort(dollar_pattern, df, "sorted_dollars.csv")

    # Plot top 10 dollar words
    plot_top_words(hashtags_df, "Top 10 Hashtags Words", "top_10_hashtags.png")
    plot_top_words(mentions_df, "Top 10 Mention Words", "top_10_mentions.png")
    plot_top_words(dollars_df, "Top 10 Dollar Words", "top_10_dollars.png")

    print(
        "The sorted counts have been saved to 'sorted_hashtags.csv', 'sorted_mentions.csv', and 'sorted_dollars.csv'"
    )
    print("The top 10 dollar words plot has been saved as 'top_10_dollars.png'")


if __name__ == "__main__":
    main()
