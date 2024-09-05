import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for index, row in alphabet.iterrows()}

def generate_phonetic():
    try:
        result = [alphabet_dict[letter] for letter in list(input("Enter a word: ").upper())]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()