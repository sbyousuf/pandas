# my_package/sort_functions.py

import pandas as pd
import re
from collections import Counter


def sort(pattern, input_file, output_file):
    

    def find_words(text):
        return re.findall(pattern, str(text))

    words = input_file["full_text"].apply(find_words).explode().dropna().tolist()
    counter = Counter(words)
    sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    indexed_list = [
        (index + 1, word, count) for index, (word, count) in enumerate(sorted_list)
    ]
    sorted_df = pd.DataFrame(indexed_list, columns=["Index", "Name", "Count"])
    sorted_df.to_csv(output_file, index=False)
    return sorted_df
