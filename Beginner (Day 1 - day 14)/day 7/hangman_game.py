import random
from hangman_art import stages,logo
from hangman_list import lists
print(logo)
print("CHÀO MỪNG BẠN ĐẾN VỚI HANGMAN!!!!")
key_word = random.choice(lists)
a = len(key_word)
mang = len(stages) - 1
key_pass = []
for _ in range(a):
    key_pass += "_"
print(" ".join(key_pass))
ket_thuc = False
while not ket_thuc:
    c = input("Mời bạn nhập 1 chữ cái:")
    for d in range(0, a):
        e = key_word[d]
        if e == c:
            key_pass[d] = e
    print(" ".join(key_pass))
    if "_" not in key_pass:
        game_finish = True
        print("Bạn thắng rồi!!!!")
    if c not in key_pass:
        print(f"Bạn chọn:{c} .Từ đó ko có trong từ khóa")
        mang -= 1
    if mang == 0:
        ket_thuc = True
        print("Bạn thua rồi!!!")
    print(stages[mang])


