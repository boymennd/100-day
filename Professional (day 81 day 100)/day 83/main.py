score_play1 = 0
score_play2 = 0
draw = 0


def base(nums):
    print(f"{nums[0]}  |  {nums[1]}  |  {nums[2]}")
    print("---------------")
    print(f"{nums[3]}  |  {nums[4]}  |  {nums[5]}")
    print("---------------")
    print(f"{nums[6]}  |  {nums[7]}  |  {nums[8]}")


def examining(nums, player_choose):
    if nums[0] == nums[1] == nums[2] == player_choose:
        result = 1
    elif nums[3] == nums[4] == nums[5] == player_choose:
        result = 1
    elif nums[6] == nums[7] == nums[8] == player_choose:
        result = 1
    elif nums[0] == nums[3] == nums[6] == player_choose:
        result = 1
    elif nums[1] == nums[4] == nums[7] == player_choose:
        result = 1
    elif nums[2] == nums[5] == nums[8] == player_choose:
        result = 1
    elif nums[0] == nums[4] == nums[8] == player_choose:
        result = 1
    elif nums[2] == nums[4] == nums[6] == player_choose:
        result = 1
    else:
        result = 0
    return result


def game_play():
    global score_play1, score_play2, draw
    nums = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    play1_choose = "X"
    play2_choose = "O"
    end = False
    print("Welcome to Tic-Tac-Toe game!")
    base(nums)
    print(f"score play 1: {score_play1} | Draw: {draw} | score play 2: {score_play2}")
    while not end:
        num_play1_choose = int(
            input(
                "Play1 turn \nWhat empty box do you want to go?(please choose 1 to 9 )"
            )
        )
        nums[num_play1_choose - 1] = play1_choose
        base(nums)
        if examining(nums, play1_choose) == 1:
            print("Player 1 win!!")
            score_play1 += 1
            base(nums)
            print(f"Play 1: {score_play1} | Draw: {draw} | Play 2: {score_play2}")
            end = True
        if " " not in nums:
            if examining(nums, play1_choose) == examining(nums, play2_choose):
                print("Draw!")
                base(nums)
                print(
                    f"score play 1: {score_play1} | Draw: {draw} | score play 2: {score_play2}"
                )
                end = True
        if not end:
            num_play2_choose = int(
                input(
                    "Play2 turn \nWhat empty box do you want to go?(please choose 1 to 9 )"
                )
            )
            nums[num_play2_choose - 1] = play2_choose
            base(nums)
        if examining(nums, play2_choose) == 1:
            print("Player 2 win!!")
            score_play2 += 1
            base(nums)
            print(
                f"score play 1: {score_play1} | Draw: {draw} | score play 2: {score_play2}"
            )
            end = True
        if " " not in nums:
            if examining(nums, play1_choose) == examining(nums, play2_choose):
                print("Draw!")
                base(nums)
                print(
                    f"score play 1: {score_play1} | Draw: {draw} | score play 2: {score_play2}"
                )
                end = True


if __name__ == "__main__":
    continues = False
    while not continues:
        game_play()
        keep = input("Do you want to continue game?(yse or no)?")
        if keep.lower() == "no":
            continues = True
