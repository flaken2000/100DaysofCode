import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha = {row.letter: row.code for (index, row) in data.iterrows()}
print(alpha)

user_word = input("Enter a word: ").upper()
new_list = [alpha[letter] for letter in user_word]
print(new_list)
