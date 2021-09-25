from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy

df = pd.read_csv("./api/final.csv", index_col=0)
df = df[df["soup"].notna()]

count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(df["soup"])

cos_sim = cosine_similarity(count_matrix, count_matrix)
df = df.reset_index()
indexes = pd.Series(df.index, index=df["title_x"])

def recommendation(title, similarity):
  index = indexes[title]
  scores = list(enumerate(similarity[index]))
  scores = sorted(scores, key=lambda x : x[1], reverse=True)
  scores = scores[1:11]
  movie_indexes = [i[0] for i in scores]
  return df["title_x"].iloc[movie_indexes]

