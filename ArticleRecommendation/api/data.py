import pandas as pd

df = pd.read_csv("./api/articles_data.csv")

data = []
for row in df.itertuples():
  data.append({
    "title": row.title,
    "contentId": row.contentId,
    "authorPersonId": row.authorPersonId,
    "timestamp": row.timestamp,
    "url": row.url,
    "lang": row.lang,
    "totalEvents": row.totalEvents,
  })