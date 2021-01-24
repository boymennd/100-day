a = float(input("moi ban nhap chieu cao:"))
b = int(input("moi ban nhap can nang::"))
BMI = b / (a/100)**2

if BMI < 16: print("ban dang qua gay do III")
elif 16 <= BMI < 17: print("ban dang gay do II")
elif 17 <= BMI < 18.5: print("ban dang gay do I")
elif 18.5 <= BMI < 25: print("ban co mot co the can doi")
elif 25 <= BMI < 30: print("ban dang thua can roi")
elif 30 <= BMI < 35: print("ban bi beo phi cap do I")
elif 35 <= BMI < 40: print("ban dang beo phi cap do II")
else: print("ban dang beo phi cap do III")