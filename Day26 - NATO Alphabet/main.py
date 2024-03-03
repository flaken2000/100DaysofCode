import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha = {row.letter: row.code for (index, row) in data.iterrows()}
print(alpha)

ValidEntry = False
while not ValidEntry:
    user_word = input("Enter a word: ").upper()
    try:
        new_list = [alpha[letter] for letter in user_word]
    except KeyError:
        print("Only letters in the alphabet please")
    else:
        ValidEntry = True
        print(new_list)
