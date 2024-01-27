import requests
from bs4 import BeautifulSoup
import datetime
############################# CSO NEWS ##################################################
class Source2:
    def getData():
        #url construction
        url3="https://www.csoonline.com/in/news"
        #fetching the web page
        r3= requests.get(url3)
        htmlcontent3= r3.content
        #parsing the web page using beautiful soup
        soup3 = BeautifulSoup(htmlcontent3, 'html.parser')
        articles3 = soup3.find_all('h3')
        article_links3=[]
        #iterating through the links and construction with append to list
        for article in articles3:
            urlraw="https://www.csoonline.com"
            alink = article.find('a')
            flink=urlraw+alink['href']
            article_links3.append(flink)
        #printing the links in the generated list
        for article_link in article_links3:
            try:
                #fetching data for a particular article
                ar3 = requests.get(article_link)
                ahtml3 = ar3.content
                #parsing the article page using beautiful soup
                articlesoup3 = BeautifulSoup(ahtml3, 'html.parser')
                Title= articlesoup3.find('h1',itemprop='headline')
                raw=articlesoup3.find('div',itemprop="articleBody")
                body=raw.find_all('p')
                print(" ")
                print(" ")
                print("Source: CSO NEWS")
                print(" ")
                print(" ")
                print("Title: "+ Title.string)
                print(" ")
                print(" ")
                print("Article Body:\n")
                for p in body:
                    if p.string != None:
                        print(p.string)
            except Exception:
                pass
 
                