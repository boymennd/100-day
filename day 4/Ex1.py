from random import choice
dam = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

la = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

keo = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a = input("Mời bạn chọn (dam, la, keo):")
ran = [dam,la, keo]
b = choice(ran)
if a == "dam":
    if b == dam:
        print(f"Bạn chọn: \n {dam} \n Máy chọn: \n {dam} \n Hòa rồi!!")
    elif b == la:
        print(f"Bạn chọn: \n {dam} \n Máy chọn: \n {la} \n Bạn thua rồi!!")
    else:
        print(f"Bạn chọn: \n {dam} \n Máy chọn: \n {keo} \n Bạn thắng rồi!!")
elif a == "la":
    if b == dam:
        print(f"Bạn chọn: \n {la} \n Máy chọn: \n {dam} \n Bạn thắng rồi!!")
    elif b == la:
        print(f"Bạn chọn: \n {la} \n Máy chọn: \n {la} \n Hòa rồi!!")
    else:
        print(f"Bạn chọn: \n {la} \n Máy chọn: \n {keo} \n Bạn thua rồi!!")
else:
    if b == dam:
        print(f"Bạn chọn: \n {keo} \n Máy chọn: \n {dam} \n Bạn thua rồi!!")
    elif b == la:
        print(f"Bạn chọn: \n {keo} \n Máy chọn: \n {la} \n Bạn thắng rồi!!")
    else:
        print(f"Bạn chọn: \n {keo} \n Máy chọn: \n {keo} \n Bạn thua rồi!!")