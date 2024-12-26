from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
movie_names = []
titles = soup.findAll(name = 'h3', class_ = 'title')
for title in titles:
    movie_names.append(title.get_text())
movie_names.reverse()
with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movie_names:
        file.write(f'{movie}\n')
print("Movies have been written to movies.txt successfully!")




