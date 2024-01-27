import requests
from bs4 import BeautifulSoup
import datetime
############################# Hacker News ##################################################
class Source1:
    def getData():
        #url construction
        date = str(datetime.date.today())
        url="https://thehackernews.com/search?updated-max="+ date +"T05:25:00-07:00&max-results=20"
        #fetching the web page
        r= requests.get(url)
        htmlcontent= r.content
        #parsing the web page using beautiful soup
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        articles = soup.find_all('a',class_="story-link")
        article_links=[]
        for article in articles:
            article_links.append(article['href'])
        for article_link in article_links:
        #fetching data for a particular article
            ar = requests.get(article_link)
            ahtml = ar.content
            #parsing the article page using beautiful soup
            articlesoup = BeautifulSoup(ahtml, 'html.parser')
            raw=articlesoup.find('div',class_="articlebody clear cf")
            body=raw.find_all('p')
            raw=articlesoup.find('div',class_="articlebody clear cf")
            img=raw.find('img')
            article_image=img['src']
            print(" ")
            print(" ")
            print("Source: HackerNews")
            print(" ")
            print(" ")
            print("Article link: ",article_link)
            print(" ")
            print(" ")
            print("Title: "+ articlesoup.title.string)
            print(" ")
            print(" ")
            print("Article Image: ",article_image)
            print(" ")
            print(" ")
            print("Article Body:\n")
            for p in body:
                if p.string != None:
                    print(" ")
                    print(" ")
                    print(p.string) 
                