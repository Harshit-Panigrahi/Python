import pandas as pd

df = pd.read_csv("./api/articles_data.csv", index_col=0)
top_20 = df[["title", "url", "timestamp", "contentType", "lang", "totalEvents"]].head(20).values.tolist()
