import requests
from bs4 import BeautifulSoup
import json


URL = "https://www.bbc.com/news"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = []

for x in range(14):
    results = soup.find_all("div", {"data-entityid":"container-top-stories#"+str(x+1)})
    for news in results:
        spanTag = news.find("span", {"class": "gs-u-vh"})
        obj = {
            "id" : x+1,
            "title" : news.h3.get_text(),
            "description" : news.p.get_text(),
            "timeZone" : news.time['datetime'],
            "updated_at" : spanTag.get_text(),
            "link" :  'https://www.bbc.com'+ news.a['href']
        }
        data.append(obj)


print('\033[1;37;43m' + '\033[1m' + "\033[1;34;43m Fetch Successfull ! \033[49m \n Write Json \n Your Data is ready \033[1;31;40m :) \033[49m")
jsonString = json.dumps(data)
jsonFile = open("latest-news.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
