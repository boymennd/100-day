def prime_number_checker(number):
    prime = True
    for a in range(2,number):
        if number % a ==0:
            prime = False
    if prime:
        print("Is prime number")
    else:
        print( "Is not prime number")

number_input = int(input("Number input:"))
prime_number_checker(number_input)