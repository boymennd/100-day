for a in range(0, 101):
  if a % 3 == 0 and a % 5 ==0:
    print("fizzbuzz")
  elif a % 5 == 0:
    print("Fizz")
  elif a % 3 == 0:
    print("buzz")
  else:
    print(a)
