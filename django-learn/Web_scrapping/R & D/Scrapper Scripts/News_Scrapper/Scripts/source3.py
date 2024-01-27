import requests
from bs4 import BeautifulSoup
import datetime
class Source3:
    def getData():
        article_links=[]
        pages=[1,2]
        for page in pages:
            #url construction
            url="https://www.securitymagazine.com/articles/topic/2189?page="+str(page)+"/"
            #fetching the webpage
            r = requests.get(url)
            htmlcontent = r.content
            #parsing the web page using beautiful soup
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            articleLinkRaw = soup.find_all('h2',class_="headline article-summary__headline")
            for articleraw in articleLinkRaw:
                articleLinkRaw2 = articleraw.find('a')
                article_link = articleLinkRaw2['href']
                article_links.append(article_link)
        for article_link in article_links:
            ar= requests.get(article_link)
            ar_content= ar.content
            articlesoup=BeautifulSoup(ar_content,'html.parser')
            titleraw=articlesoup.find('h1',class_="headline")
            title=titleraw.string
            print(" ")
            print(" ")
            print("Article link: ",article_link)
            print(" ")
            print(" ")
            print("Source: Security Magazine")
            print(" ")
            print(" ")
            print("Title: ",title)
            body = "NA"
            print("Article Body: ", body)
            print(" ")
            print(" ")
        


