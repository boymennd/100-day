import random
def card_take():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card
def sum_card(cards):
    if sum(cards) >21 and 11 in cards:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
    return sum(cards)
end = False
while not end:
    you = []
    computer = []
    for i in range(2):
        you.append(card_take())
        computer.append(card_take())
    win = False
    while not win:
        your_score = sum_card(you)
        computer_score = sum_card(computer)
        def prints():
            print(f"Your final hand: {you}, Your final score: {your_score}")
            print(f"Computer's final hand: {computer}. Computer final score: {computer_score}")
        print(f"Your cards: {you}. current score: {your_score}")
        print(f"Computer's first cards: {computer[0]}")
        while computer_score < 21:
            computer.append(card_take())
            computer_score = sum_card(computer)
        continues = input("Type 'y' to get another cards or type 'n' to pass:")
        if continues == "y" and len(you) < 4:
            you.append(card_take())
            your_score = sum_card(you)
            if your_score > 21:
                prints()
                print("You lose !!!")
                win = True
        else:
            if your_score == 21:
                prints()
                print("Congratulations! You got a Blackjack!")
            elif computer_score == 21:
                prints()
                print("Sorry, you lose. The computer got a blackjack")
            elif your_score > 21:
                prints()
                print("Sorry. You busted. You lose")
            elif computer_score > 21:
                prints()
                print("Computer busted. you win!!")
            elif your_score > computer_score:
                prints()
                print("You win !!!")
            elif computer_score < your_score:
                prints()
                print("You lose !!!")
            elif computer_score == your_score:
                prints()
                print("Draw!!!")
            win = True
    ends = input("Do you want to play a game of Blackjack again? Type 'y' or 'n':")
    if ends == 'n':
        end = True