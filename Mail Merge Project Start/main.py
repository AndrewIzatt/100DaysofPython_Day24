#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("Input/Letters/starting_letter.txt") as letter:
    letter_list = letter.readlines()
    # print(letter_list)
    with open("Input/Names/invited_names.txt") as names:
        individual_names = names.readlines()
    for name in individual_names:
        new_letter = letter_list.copy()
        cleaned_name = name.strip("\n")
        edited_line = new_letter[0].replace("[name]", cleaned_name)
        new_letter.pop(0)
        new_letter.insert(0, edited_line)
        with open(f"Output/ReadyToSend/letter_for_{cleaned_name}.txt", "w") as invitation:
            for line in new_letter:
                invitation.write(line)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp