from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

story_link = soup.find(name='span', class_='titleline')
story_link_title = story_link.find(name='a')
print(story_link_title.get_text())
print(story_link_title.get('href'))

story_score = soup.find(name='span', class_='score')
print(story_score.get_text())
