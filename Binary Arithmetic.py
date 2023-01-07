def menu():
    print("""
            Choose the Option from the menu to perform the respected task...
            0> Exit
            1> Binary Addition
            2> Binary Subtraction
            3> Binary to Multiplication
            4> Octal to Division
        """)
    return int(input("Enter the Option: "))


def binary_to_decimal(number):
    number = number[::-1]
    result = 0
    count = 0
    for n in number:
        if n == "1":
            result += 2 ** int(count)
        count += 1
    return result


def decimal_to_binary(number):
    result = ""
    while number > 0:
        if number % 2 == 1:
            result = result + "1"
        elif number % 2 == 0:
            result = result + "0"
        elif number == 0:
            exit()
        number = int(number / 2)

    return result[::-1]


def binary_addition():
    number1 = binary_to_decimal(input("Enter the first number : "))
    number2 = binary_to_decimal(input("Enter the Second number : "))
    return decimal_to_binary(number1 + number2)


def binary_subtraction():
    number1 = binary_to_decimal(input("Enter the first number : "))
    number2 = binary_to_decimal(input("Enter the Second number : "))
    return decimal_to_binary(number1 - number2)


def binary_multiplication():
    number1 = binary_to_decimal(input("Enter the first number : "))
    number2 = binary_to_decimal(input("Enter the Second number : "))
    return decimal_to_binary(number1 * number2)


def binary_division():
    number1 = binary_to_decimal(input("Enter the first number : "))
    number2 = binary_to_decimal(input("Enter the Second number : "))
    return decimal_to_binary(number1 / number2)


i = 1
while i == 1:
    option = menu()

    if option == 0:
        exit()
    elif option == 1:
        print("Binary Addition : ", binary_addition())
    elif option == 2:
        print("Binary Subtraction : ", binary_subtraction())
    elif option == 3:
        print("Binary Multiplication : ", binary_multiplication())
    elif option == 4:
        print("Octal Division : ", binary_division())
