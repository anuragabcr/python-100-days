import requests
from bs4 import BeautifulSoup

date = input('Enter date in (YYYY-MM-DD) format:- ')
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
songsList = soup.select("li ul li h3")

song_names = [song.get_text(strip=True) for song in songsList]
print(song_names)
