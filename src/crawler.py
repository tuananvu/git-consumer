import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://syneren.com/opportunities/careers"
#html = urlopen("https://en.wikipedia.org/wiki/Extraversion_and_introversion")
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
bsObj = BeautifulSoup(page.text,"html.parser")
#bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
