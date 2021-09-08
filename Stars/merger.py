import csv

rows1 = []
rows2 = []

with open("./data1.csv", 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    rows1.append(row)

with open("./data2.csv", 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    rows2.append(row)

headers = rows1[0]
del headers[0]
headers.append("gravity")
data1 = rows1[1:]
data2 = rows2[1:]

temp1 = rows1[1:]
for star in temp1:
  try:
    star[2] = float(star[2])
    star[3] = float(star[3])
    star[4] = float(star[4])
    del star[0]
  except:
    data1.remove(star)

temp2 = rows2[1:]
for star in temp2:
  try:
    star[2] = float(star[2])
    star[3] = float(star[3])*0.000954588
    star[4] = float(star[4])*0.102763
    del star[0]
  except:
    data2.remove(star)

data = data1 + data2

for star in data:
  mass = star[2] * 1.989e+30
  radius = star[3] * 6.957e+8
  g = (6.674e-11 * mass)/(radius**2)
  print(star[0], g)
  star.append(g)


with open('./merged-data.csv', 'a+')as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(data)
