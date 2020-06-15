import json
import requests
from bs4 import BeautifulSoup

all_items = []
url = "https://www.abapzombie.com/page/1/"

for i in range(21):
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')

    page = soup.find(class_="next").get('href')
    url = page
    items = soup.find_all(class_="bam-entry")

    for item in items:
        thumb = item.a.img["src"]
        link = item.a.get('href'),
        title = item.h2.text,
        description = item.p
        all_items.append({
            "thumb": thumb,
            "link": link,
            "title": title,
            "description": description.text
        })

with open('posts.json', 'w') as json_file:
    json.dump(all_items, json_file, indent=4)
