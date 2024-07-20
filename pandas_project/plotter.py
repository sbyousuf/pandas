import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_top_words(df, title, filename):
    top_10 = df.head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_10, x="Count", y="Name", palette="viridis")
    plt.title(title)
    plt.xlabel("Count")
    plt.ylabel("Word")
    plt.tight_layout()
    result_dir = "sample_result"
    file_path = os.path.join(result_dir, filename)
    plt.savefig(file_path)
    plt.show()
