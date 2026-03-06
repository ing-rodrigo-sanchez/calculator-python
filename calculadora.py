import math


def add(a, b):
    print(f"Result: {a + b}")


def subtract(a, b):
    print(f"Result: {a - b}")


def multiplication(a, b):
    print(f"Result: {a * b}")


def division(a, b):
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("You cannot divide by zero.")


def empowerment(a, b):
    print(f"Result: {a ** b}")


def squared_root(a):
    if a >= 0:
        print(f"Result: {math.sqrt(a)}")
    else:
        print("The base cannot be negative.")


def logarithm(a, b):
    if a > 0 and b > 0 and b != 1:
        print(f"Result: {math.log(a, b)}")
    else:
        print("Invalid values for logarithm.")


operations = {
    1: add,
    2: subtract,
    3: multiplication,
    4: division,
    5: empowerment,
    6: squared_root,
    7: logarithm,
}

while True:

    for number, operation in operations.items():
        print(f"{number}. {operation.__name__}")

    while True:
        try:
            option = int(input("Number option: "))
            if option in operations:
                break

            else:
                print("Enter a number from the list")

        except ValueError:
            print("Enter only numbers")

    while True:
        try:
            if option == 6:
                number_1 = float(input("Enter the base: "))
                break

            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            break

        except ValueError:
            print("Enter only numbers")

    if option == 6:
        operations[option](number_1)

    else:
        operations[option](number_1, number_2)

    repeat = input("Would you like to use the calculator again? (yes/no): ")

    if repeat.lower() == "no":
        break
