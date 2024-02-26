# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

output_file_name = "letter_for_"

with open("./Input/Names/invited_names.txt") as file:
    contents = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file_names:
    starting_letter = file_names.read()

# Loop through the names
for name in contents:
    name = name.strip()
    contents = starting_letter.replace("[name]", name)
    final_file_name = output_file_name + name + ".txt"
    with open(f"./Output/ReadyToSend/{final_file_name}", mode="w") as file_letters:
        file_letters.write(contents)



