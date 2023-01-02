from bs4 import BeautifulSoup
from urllib import request

with request.urlopen("https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())
