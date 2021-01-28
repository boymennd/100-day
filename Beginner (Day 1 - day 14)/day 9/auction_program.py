import os
program = []
def add_new_player(new_name,new_bid):
    new_player = {}
    new_player["name"] = new_name
    new_player["bid"] = new_bid
    program.append(new_player)

end = False
while not end:
    name1 = input("What is your name? \n")
    bid1  = int(input("What is your bid ? \n $"))
    add_new_player(name1,bid1)
    next = input("Are there any other bidder:(yes or no) \n")
    os.system('cls')
    if next == "no":
        end = True
        max = 0
        for i in range(0,len(program)):
            if program[i]["bid"] > max:
                max = program[i]["bid"]
                a = i
        c = str(program[a]["bid"])
        print("The winner is " + program[a]["name"] + "with a bid of $" + c )
