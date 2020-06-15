import json
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.abapzombie.com/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all(class_="bam-entry")

all_items = []
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

print(items)
print(all_items)

with open('posts.json', 'w') as json_file:
    json.dump(all_items, json_file, indent=3, ensure_ascii=False)