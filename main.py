from bs4 import BeautifulSoup
import requests
import lxml
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")
print(soup)

title_tag = soup.find_all(name="h3", class_="title")

movie_title_list = [title.getText() for title in title_tag]
movie_title_list.reverse()
print(movie_title_list)

with open("movies.txt", "w") as f:
    for movie in movie_title_list:
        f.write(movie)
        f.write("\n")