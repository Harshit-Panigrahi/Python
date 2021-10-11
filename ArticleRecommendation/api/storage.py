from data import data

names = []
for i in data:
  names.append(i["title"])

storage = {
  "starred": [],
  "all": names
}