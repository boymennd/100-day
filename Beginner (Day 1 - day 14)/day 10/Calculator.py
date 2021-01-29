
def add(a1,a2):
    return a1 + a2
def subtract(a1,a2):
    return a1 - a2
def multiply(a1,a2):
    return a1 * a2
def divide(a1,a2):
    return a1 / a2
end = False
while not end:
    a = float(input("What's the first number?"))
    print(" + \n - \n * \n /")
    continues = False
    while not continues:
        calculation = input("Pick on calculation:")
        b = float(input("What's the next number?"))
        if calculation == "+":
            d = float(add(a,b))
            print(f"{a} + {b} = {d}")
        elif calculation == "-":
            d = float(subtract(a,b))
            print(f"{a} - {b} = {d}")
        elif calculation == "*":
            d = float(multiply(a,b))
            print(f"{a} * {b} = {d}")
        else:
            d = divide(a,b)
            print(f"{a} / {b} = {d}")
        c = input(f"Type 'y' to continue with {d}, or type 'n' to start a new calculation:")
        if c == "y":
            a = d
        else:
            continues = True
