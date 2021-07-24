from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

STARTURL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("./chromedriver")
browser.get(STARTURL)
time.sleep(10)

planetData = []
newPlanetData = []
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", "planet_type", "planet_radius", "orbital_radius"]
def scrape():
  for i in range(444):
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for ul_tag in soup.find_all("ul", attrs={'class': "exoplanet"}):
      li_tags = ul_tag.find_all("li")
      tempList = []
      for index, li_tag in enumerate(li_tags):
        if index == 0:
          tempList.append(li_tag.find_all('a')[0].contents[0])
        else:
          try:
            tempList.append(li_tag.contents[0])
          except:
            tempList.append('')
            
      hyperlink_li_tag = li_tags[0]
      tempList.append("https://exoplanets.nasa.gov/"+hyperlink_li_tag.find_all("a", href='true')[0]["href"])

      planetData.append(tempList)
    browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

scrape()

with open('./data.csv', 'w') as f:
  csvwriter = csv.writer(f)
  csvwriter.writerow(headers)
