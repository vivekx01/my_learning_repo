from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
#url of the page that we want to Scarpe
#+str() is used to convert int datatype of the page no. and concatenate that to a URL for pagination purposes.
url = 'https://thehackernews.com/search?updated-max=2021-08-29T05:25:00-07:00&max-results=20'
#Use the browser to get the URL. This is a suspicious command that might blow up.
page = requests.get(url)
print(page.text)






# import newspaper

# # import nltk
# # nltk.download('punkt')

# # article= Article('https://www.securitymagazine.com/articles/95793-data-breaches-in-the-first-half-of-2021-exposed-188-billion-records')
# # article.download()
# # article.parse()
# # article.nlp()
# # print('Data retrieved successfully')
# # print(article.title)
# # print(article.authors)

# hck = newspaper.build("https://cnn.com")

# for article in hck.articles:
#     print (article.url)
