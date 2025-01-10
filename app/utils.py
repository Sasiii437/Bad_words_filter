# import pandas as pd
# import re

# # Load bad words
# badwords = pd.read_csv("data/bad-words.csv").tolist()

# def filter_badwords(sentence):
#     words = sentence.split()
#     filtered_words = [
#         "***" if re.sub(r'[^\w]', '', word.lower()) in badwords else word
#         for word in words
#     ]
#     return " ".join(filtered_words)
import csv

def load_badwords(filepath):
    with open(filepath, newline='') as csvfile:
        return [row[0].strip().lower() for row in csv.reader(csvfile)]

BADWORDS = load_badwords('data/bad-words.csv')

def clean_sentence(sentence):
    words = sentence.split()
    sanitized = [
        "***" if word.lower() in BADWORDS else word
        for word in words
    ]
    return ' '.join(sanitized)
