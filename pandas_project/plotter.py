import matplotlib.pyplot as plt
import seaborn as sns


def plot_top_words(df, title, filename):
    top_10 = df.head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_10, x="Count", y="Name", palette="viridis")
    plt.title(title)
    plt.xlabel("Count")
    plt.ylabel("Word")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
