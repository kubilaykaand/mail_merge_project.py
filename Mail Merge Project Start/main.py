PLACEHOLDER ="[name]"
#prep with pseudocode
    # names=open("./Input/Names/invited_names.txt")
    # letter=open("./Input/Letters/starting_letter.txt")
    # letters_list=[]
    # for i in range(0,7):
    #     current_name= names.readline()
    #     letters_list.append(letter.replace("[name]",current_name))

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER , stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)
