name_list = []

with open("Input/Names/invited_names.txt","r") as f:
    name_list.extend(f.readlines())
with open(f"Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in name_list:
        new_name = name.strip()
        new_letter = letter.replace("[name]",new_name)
        with open(f"Output/ReadyToSend/Letter_for_{new_name}.txt","w") as complete_file:
            complete_file.write(new_letter)