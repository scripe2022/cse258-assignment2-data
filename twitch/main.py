#!/home/jyh/ucsd/fa24/cse258/cse258venv/bin/python3
# run  := python3 main.py
# dir  := .
# kid  :=

import pandas as pd
import re
import pickle

data = pd.read_csv("chat.csv")
# for row in data.itertuples():
sentences = list(data["message"].values)
sentences = [str(i) for i in sentences if type(i) == str]

def remove_mentions(comment):
    cleaned_comment = re.sub(r'@\w+', '', comment)
    cleaned_comment = re.sub(r'\s+', ' ', cleaned_comment).strip()
    return cleaned_comment

pickle.dump(sentences, open("tokens.pkl", "wb"))

# sentences = [remove_mentions(str(i)) for i in sentences]
# lens = [len(i.split()) for i in sentences]
# print("max len: ", max(lens))
# print("min len: ", min(lens))

# for i in sentences:
#     print(remove_mentions(str(i)))
#     print(i)
