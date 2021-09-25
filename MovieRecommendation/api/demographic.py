import pandas as pd

df = pd.read_csv("./api/final_data.csv", index_col=0)

C = df["vote_average"].mean()
M = df["vote_count"].quantile(0.9)

q_movies = df.copy().loc[df["vote_count"] >= M]

def get_rating(x):
  V = x["vote_count"]
  R = x["vote_average"]
  return (V / (V + M) * R) + (M / (V + M) * C)

q_movies["score"] = q_movies.apply(get_rating, axis=1)
q_movies = q_movies.sort_values("score", ascending=False)
output = q_movies[["title", "poster_link", "score", "release_date", "runtime", "vote_average", "overview"]].head(20).values.tolist()

print(output[0])