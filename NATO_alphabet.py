import pandas as pd

df = pd.read_csv(r"data/nato_phonetic_alphabet.csv")
phonetic = {row['letter']: row['code'] for index, row in df.iterrows()}
name = input('Enter a name: ')
phonetic_name = [phonetic[letter.capitalize()] for letter in name]
print(phonetic_name)
