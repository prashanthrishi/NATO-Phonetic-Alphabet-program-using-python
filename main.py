import pandas

# Read the CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
words = input("Enter a word: ").upper()
output_list = [new_dict[letter] for letter in words]
print(output_list)
