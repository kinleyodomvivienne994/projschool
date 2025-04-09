import os
import requests
from bs4 import BeautifulSoup

def scrape_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("div", {"class": "article-content"})
    return data.text

url = "https://example.com"
info = scrape_info(url)

print(info)
