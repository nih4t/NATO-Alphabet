import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for index, row in alphabet.iterrows()}

result = [alphabet_dict[letter] for letter in list(input("Enter a word: ").upper())]
print(result)