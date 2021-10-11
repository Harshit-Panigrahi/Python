import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("./api/articles_data.csv", index_col=0)

count_vect = CountVectorizer(stop_words="english")
matrix = count_vect.fit_transform(df["title"])
cos_sim = cosine_similarity(matrix, matrix)

df = df.reset_index()
indexes = pd.Series(df.index, index=df["title"])

def recommend(title):
  index = indexes[title]
  scores = list(enumerate(cos_sim[index]))
  scores = sorted(scores, key=lambda x : x[1], reverse=True)
  scores = scores[1:11]
  article_idxes = [i[0] for i in scores]
  return df["title"].iloc[article_idxes]