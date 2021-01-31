import random
def card_take():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card
    cards.remove(1)
def card_start():
    start = []
    for i in range(2):
        start.append(card_take())
    return start
def the_score(c):
