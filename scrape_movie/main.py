import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.timeout.com/film/best-movies-of-all-time')
content = response.text
soup = BeautifulSoup(content, 'html.parser')
movie_titles = soup.find_all(name='h3', class_='_h3_cuogz_1')
with open('movie.txt', 'a') as file:
    for movie in movie_titles:
        file.write(f"{movie.get_text()}\n")
