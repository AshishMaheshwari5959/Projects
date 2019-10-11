'''import requests
from bs4 import BeautifulSoup
url='http://www.nytimes.com'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n"," ").strip())
    else:
        print(story_heading.contents[0].strip())

print("no output")
'''
import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text,"html.parser")
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
     ttl_lst.append(row.text)

print (ttl_lst)
