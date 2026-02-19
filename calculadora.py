import math


def operations():
    while True:
        try:
            quantity = int(input("Enter the number of operations to be performed: "))
            break
        except ValueError:
            print("Enter numbers only")

    if option == 1:
        accountant = 0

        for _ in range(quantity):
            while True:
                try:
                    value = float(input("Enter the numerical value: "))
                    break

                except ValueError:
                    print("Enter numbers only")

            accountant += value
        print(f"The value of the sum is: {accountant:.1f}")

    elif option == 2:
        accountant = 1

        for _ in range(quantity):
            while True:
                try:
                    value = float(input("Enter the numerical value: "))
                    break

                except ValueError:
                    print("Enter numbers only")

            accountant *= value
        print(f"The value of the multiplication is: {accountant:.1f}")

    elif option == 3:
        for _ in range(quantity):
            while True:
                try:
                    dividend = float(input("Enter the dividend: "))
                    divider = float(input("Enter the divisor: "))
                    break

                except ValueError:
                    print("Enter numbers only")

            if divider == 0:
                print("The divisor cannot be equal to 0.")
            else:
                resultado = dividend / divider
                print(f"The value of the division is: {resultado:.3f}")

    elif option == 4:
        for _ in range(quantity):
            while True:
                try:
                    base = float(input("Enter the base: "))
                    exponent = float(input("Enter the exponent: "))
                    break

                except ValueError:
                    print("Enter numbers only")

            outcome = base**exponent
            print(f"The power value is: {outcome:.1f}")

    elif option == 5:
        for _ in range(quantity):
            while True:
                try:
                    index = float(input("Enter the root index: "))
                    radicand = float(input("Enter the radicand of the root: "))
                    break

                except ValueError:
                    print("Enter numbers only")

            if index != 0:
                outcome = radicand ** (1 / index)
                print(f"The value of the root is: {outcome:.1f}")
            else:
                print("Invalid mathematical operation")

    elif option == 6:
        for _ in range(quantity):
            while True:
                try:
                    argument = float(input("Enter the argument of the logarithm: "))
                    base = float(input("Enter the base of the logarithm: "))
                    break

                except ValueError:
                    print("Enter numbers only")

            if argument > 0 and base > 0 and base != 1:
                outcome = math.log(argument, base)
                print(f"The value of the logarithm is: {outcome:.1f}")
            else:
                print("Invalid mathematical operation")

    else:
        print("Invalid operation")
        print("Enter only whole numbers between 1 and 6")
        exit()


name = input("Enter your name: ")
print(f"Welcome {name} to your calculator")

print(
    "1. Addition and/or Subtraction \n",
    "2. Multiplication \n",
    "3. Division \n",
    "4. Exponentiation \n",
    "5. Root \n",
    "6. Logarithm \n",
)

while True:
    try:
        option = int(input("Select the number of the desired operation: "))
        break

    except ValueError:
        print("Enter only numbers")

operations()

print(f"Thank you very much {name}, for using the app ;)")
