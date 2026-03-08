import math


def add(a, b):
    return f"Result: {a + b}"


def subtract(a, b):
    return f"Result: {a - b}"


def multiplication(a, b):
    return f"Result: {a * b}"


def division(a, b):
    if b != 0:
        return f"Result: {a / b}"
    else:
        return "You cannot divide by zero."


def exponentiation(a, b):
    return f"Result: {math.pow(a, b)}"


def squared_root(a):
    if a >= 0:
        return f"Result: {math.sqrt(a)}"
    else:
        return "The base cannot be negative."


def logarithm(a, b):
    if a > 0 and b > 0 and b != 1:
        return f"Result: {math.log(a, b)}"
    else:
        return "Invalid values for logarithm."


def absolute_value(a):
    return f"Result: {math.fabs(a)}"


def sine(a):
    radians = math.radians(a)
    return f"Result: {math.sin(radians):.1f}"


def cosine(a):
    radians = math.radians(a)
    return f"Result: {math.cos(radians):.1f}"


def tangent(a):
    if a % 180 == 90:
        return "undefined result"

    radians = math.radians(a)
    return f"Result: {math.tan(radians):.1f}"


def factorial(a):
    if a >= 0:
        return f"Result: {math.factorial(a)}"
    else:
        return "Invalid values for factorial"


def combinatorics(a, b):
    if a >= b and a >= 0 and b >= 0:
        return f"Result: {math.comb(a, b)}"
    else:
        return "Invalid values for combinatorics."


def permutation(a, b):
    if a >= b and a >= 0 and b >= 0:
        return f"Result: {math.perm(a, b)}"
    else:
        return "Invalid values for permutation."


print("Calculator")
operations = {
    1: add,
    2: subtract,
    3: multiplication,
    4: division,
    5: exponentiation,
    6: squared_root,
    7: logarithm,
    8: absolute_value,
    9: sine,
    10: cosine,
    11: tangent,
    12: factorial,
    13: combinatorics,
    14: permutation,
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
            if option in [6, 8, 9, 10, 11]:
                number_1 = float(input("Enter the number: "))
                break

            elif option in [12]:
                number_1 = int(input("Enter the number: "))
                break

            elif option in [13, 14]:
                number_1 = int(input("Total items (n): "))
                number_2 = int(input("Elements to choose from (k): "))
                break

            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            break

        except ValueError:
            print("Enter only numbers")

    if option in [6, 8, 9, 10, 11, 12]:
        result = operations[option](number_1)
        print(result)

    else:
        result = operations[option](number_1, number_2)
        print(result)

    repeat = input("Would you like to use the calculator again? (yes/no): ")

    if repeat.lower() == "no":
        break
