from random import choice
from gane_data import data


def reload(compare_A, against_B):
    if compare_A == against_B:
        against_B = choice(data)
        return against_B


def check(compare_A, against_B):
    if compare_A["follower_count"] > against_B["follower_count"]:
        return "a"
    else:
        return "b"


def new_acc(compare_A, against_B):
    if compare_A["follower_count"] > against_B["follower_count"]:
        return compare_A
    else:
        return against_B


def play_game(compare_A, against_B):
    point = 0
    end = False
    while not end:
        print(
            f"Compare A :{compare_A['name']}, {compare_A['description']}, {compare_A['country']}"
        )
        print("\nVS\n")
        print(
            f"Against B :{against_B['name']}, {against_B['description']}, {compare_A['country']}"
        )
        choose = input("Who has more follower? Type 'A' or 'B'").lower()
        if choose == check(compare_A, against_B):
            point += 1
            compare_A = new_acc(compare_A, against_B)
            against_B = choice(data)
            reload(compare_A,against_B)
            print(f"You right. Your sore is: {point}")
        else:
            print(f"Sorry, that's wrong. final point: {point}")
            end = True


if __name__ == "__main__":
    print("Welcome to higher lower game !!!!!")
    compare_A = choice(data)
    against_B = choice(data)
    reload(compare_A, against_B)
    play_game(compare_A, against_B)
