from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")

print(soup)
