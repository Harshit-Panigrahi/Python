import csv

rows1 = []
with open("./movies_data.csv", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    rows1.append(row)

rows2 = []
with open("./movies_images.csv", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    rows2.append(row)

headers = rows1[0]
headers.append("movie_poster_link")


data = []
for movie_item in rows1:
  poster_found = any(movie_item[8] in links for links in rows2)
  if poster_found:
    for movie_link_item in rows2:
      if movie_item[8] == movie_link_item[0]:
        movie_item.append(movie_link_item[1])
      if len(movie_item) == 28:
        data.append(movie_item)

with open("final.csv", "a+") as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerow(data)