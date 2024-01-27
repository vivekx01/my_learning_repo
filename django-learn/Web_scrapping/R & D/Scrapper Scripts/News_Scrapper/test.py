import requests
from bs4 import BeautifulSoup
import datetime
#url construction
url = "https://grahamcluley.com/"
#fetching the webpage
r = requests.get(url)
htmlcontent = r.content
#parsing the webpage using beautiful soup
soup = BeautifulSoup(htmlcontent,'html.parser')
articleraw = soup.find_all('a',rel="bookmark")
article_links=[]
article_titles=[]
for link in articleraw:
    article_links.append(link['href'])
for title in articleraw:
        article_titles.append(title.string)
for article_link in article_links:
    # for article_title in article_titles:
    print("Article Link:",article_link)
    print(" ")
    print(" ")
    print("Source: Graham Cluley")
    print(" ")
    print(" ")
    print("Article Title: ",article_title)
    try:
        arget=requests.get(article_link)
        arcontent = arget.content
        articlesoup= BeautifulSoup(arcontent,'html.parser')
        article_raw= articlesoup.find_all('p')
        print("Article Body: \n")
        for content in article_raw:
            if content!=None:
                print(content.string)
    except:
        print("Article Body: NA")
    print(" ")
    print(" ")
