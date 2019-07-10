#This is a Py_Webscrape where program will scrape a quote from brainyquote.com

#pip install beautifulsoup4
from bs4 import BeautifulSoup

#pip install requests
#sudo pip install requests(unix)
import requests

#http Req
res = requests.get('https://www.brainyquote.com/quote_of_the_day')

#soupObject
soup = BeautifulSoup(res.text, 'lxml')

#path of the relavant quote
image_quote = soup.find('img', {'class': 'p-qotd bqPhotoDefault bqPhotoDefaultFw img-responsive'})
print(image_quote['alt'])