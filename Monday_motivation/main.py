import random
import datetime

with open('quotes.txt', 'r') as file:
    content = file.readlines()

date = datetime.datetime.now()
if date.weekday() == 2:
    print(random.choice(content))
