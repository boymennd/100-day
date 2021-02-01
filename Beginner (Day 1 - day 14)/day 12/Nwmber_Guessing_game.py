import random
def play_game(level):
    a = random.randint(1, 100)
    while level != 0:
        print(f"You have {level} attempts remaining to get the number")
        c = int(input("Make a guess"))
        if c == a:
           print(f"You got it .The number is {a}!")
           level = 0
        elif c > a:
            print(f"Too high")
            level -= 1
        else:
            print(f"Too low")
            level -= 1
    if c != a:
        print("You've run out of guess. You lose!!")

again = False
while not again:
    print("Welcome to Number Guessing game! ")
    print("I'm thinking of number between 1 and 100?")
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        play_game(10)
    else:
        play_game(5)
    next = input("Run again. Type 'y' or 'n'")
    if next == "n":
        again = True