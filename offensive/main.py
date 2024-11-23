#!/home/jyh/ucsd/fa24/cse258/cse258venv/bin/python3
# run  := python3 main.py
# dir  := .
# kid  :=

import pandas as pd
import html
import re
import pickle

data = pd.read_csv("labeled_data.csv")


def twitter_mentions(comment):
    comment = re.sub(r"(https?://|www\.)[^\s]+", "", comment)
    comment = re.sub(r"@\S+:\s", "", comment)
    comment = re.sub(r"@\S+:", "", comment)
    comment = re.sub(r"@\S+\s", "", comment)
    comment = re.sub(r"@\S+", "", comment)
    comment = re.sub(r"\s+", " ", comment).strip()
    return comment


sentences = data["tweet"].values
# for row in data.itertuples():
#     print(html.unescape(twitter_mentions(row.tweet)))
pickle.dump(sentences, open("tokens.pkl", "wb"))
