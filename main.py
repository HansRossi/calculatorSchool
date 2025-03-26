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
        print("Goodbye!")

calculator()
        