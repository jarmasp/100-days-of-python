import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:

phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('enter a word : ').upper()

print([phonetic_alphabet[letter] for letter in word])
