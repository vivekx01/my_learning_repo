import requests
from bs4 import BeautifulSoup
import datetime
class Source5:
    def getData():
        #url construction
        url = "https://www.cnbc.com/cybersecurity/"
        #fetching the webpage
        r = requests.get(url)
        htmlcontent = r.content
        #parsing the webpage using beautiful soup
        soup = BeautifulSoup(htmlcontent,'html.parser')
        articleraw = soup.find_all('div',class_="Card-titleContainer")
        for article in articleraw:
            linksraw= article.find('a')
            print(" ")
            print("Article link: ",linksraw['href'])
            print("Source: CNBC News")
            print("Article title: ",article.string)
            print("Article Body: NA")
            print(" ")