import math

options = """
-------------------------------------
Chooese the right option to calculate
-------------------------------------
0 : Addition
1 : Subtraction
2 : Multiplication
3 : Division
4 : Modulus
5 : Power
6 : Factorial
7 : Square root
8 : Cube root
"""


def get_input():
    number2 = int(input("Enter second number: "))
    number1 = int(input("Enter first number:  "))
    return number1, number2


print(options)
choice = int(input("\nYour Choice: "))
if choice == 0:
    x = get_input()
    print(x[0] + x[1])
elif choice == 1:
    x = get_input()
    print(x[0] - x[1])
elif choice == 2:
    x = get_input()
    print(x[0] * x[1])
elif choice == 3:
    x = get_input()
    print(x[0] / x[1])
elif choice == 4:
    x = get_input()
    print(x[0] % x[1])
elif choice == 5:
    x = get_input()
    print(x[0] ** x[1])
elif choice == 7:
    x = int(input("Enter a number: "))
    print(math.sqrt(x))
elif choice == 8:
    x = int(input("Enter a number: "))
    print(math.cbrt(x))
else:
    print("Wrong Choice choosen.")
