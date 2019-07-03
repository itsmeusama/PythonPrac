from bs4 import BeautifulSoup
import requests
#http Req
res = requests.get('https://www.brainyquote.com/quote_of_the_day')

#soupObject
soup = BeautifulSoup(res.text, 'lxml')

#path of the relavant quote
image_quote = soup.find('img', {'class': 'p-qotd bqPhotoDefault bqPhotoDefaultFw img-responsive'})
print(image_quote['alt'])