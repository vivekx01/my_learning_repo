# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

import requests
from bs4 import BeautifulSoup
url = "https://thehackernews.com/"
# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

# Step 3: HTML tree traversal
# Commonly used types of objects:
# print (type(title)) 1.Tag
# print (type(title.string)) 2. NavigableString
# print (type(soup)) 3.BeautifulSoup
# 4. Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p.string)
#exit()

title = soup.title

#Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)
#Get all the anchors from the page
a = soup.find_all('a')
# print(a) 

#Get first element from the html page
print(soup.find('p'))

#Get classes of any element in the html page
print(soup.find('p')['class'])

# find all the elements with class lead
print (soup.find_all('p', class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())

all_links = set()
#get all the links from the page:
for link in a:
    if(link.get('href') != '#'):
        linkText = "https://thehackernews.com/" + link.get('href')
        all_links.add(link)
        print(linkText)

# .contents - A tag's children are available as a list (stored in memory) (Slow for long pages)
# .children - A tag's children are available as a generator (not stored but can be retrieved to iterate) (faster for long pages)    
navsupportcontent = soup.find(id="navsupportcontent")
# for elem in (navsupportcontent.contents):
#     print(elem)

# for item in navsupportcontent.stripped_strings:
#     print(item)

# print(navsupportcontent.parent)
# for item in navsupportcontent.parents:
#     print(item.name)

# print(navsupportcontent.next_sibling)
# print(navsupportcontent.previous_sibling)
# elem= soup.select('#loginModal')
# print(elem)
# elem= soup.select('.modal-footer')
# print(elem)
