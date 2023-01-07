def menu():
    print("""
            Choose the Option from the menu to perform the respected task...
            0> Exit
            1> Binary to Decimal
            2> Binary to Octal
            3> Binary to Hexadecimal
            4> Octal to Binary
            5> Octal to Decimal
            6> Octal to Hexadecimal
            7> Decimal to Binary
            8> Decimal to Octal
            9> Decimal to Hexadecimal
            10> Hexadecimal to Binary
            11> Hexadecimal to Octal
            12> Hexadecimal to Decimal
        """)
    return int(input("Enter the Option: "))


def get_number():
    return input("Enter the number: ")


def bin_to_dec(number):
    number = number[::-1]
    result = 0
    count = 0
    for n in number:
        if n == "1":
            result += 2 ** int(count)
        count += 1
    return result


def bin_to_oct(number):
    result = ""
    while number > 8:
        if number % 8 == 0:
            result = result + str(0)
        else:
            result = result + str(number % 8)
        number = int(number / 8)
        if number != 0 and number < 8:
            result = result + str(number)
    return result[::-1]


def bin_to_hex(number):
    result = ""
    while number > 16:
        if number % 16 == 0:
            result = result + str(0)
        else:
            result = result + str(number % 16)
        number = int(number / 16)
        if number != 0 and number < 16:
            result = result + str(number)
    return result[::-1]


def oct_to_bin(number):
    oct_bin_list = ['000', '001', '010', '011', '100', '101', '110', '111']
    result = ""
    for n in number:
        result = result + oct_bin_list[int(n)] + ' '
    return result


def oct_to_dec(number):
    number = number[::-1]
    result = 0
    count = 0
    for n in number:
        result += int(n) * (8 ** int(count))
        count += 1
    return result


def oct_to_hex(number):
    result = ""
    hex_dec_list = ['0', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while number > 16:
        if number % 16 == 0:
            result = result + str(0)
        else:
            result = result + str(number % 16)
        number = int(number / 16)
        if number != 0 and number < 16:
            result = result + str(number)
    return result[::-1]


def dec_to_bin(number, base):
    result = ""
    while number > 0:
        if number % 2 == 1:
            result = result + "1"
        elif number % 2 == 0:
            result = result + "0"
        elif number == 0:
            exit()
        number = int(number / 2)

    if base == 0:
        return result[::-1]
    if base == 16:
        return result[::-1].rjust(4, '0')
    if base == 8:
        return result[::-1].rjust(3, '0')


def dec_to_oct(number):
    result = ""
    while number > 8:
        if number % 8 == 0:
            result = result + str(0)
        else:
            result = result + str(number % 8)
        number = int(number / 8)
        if number != 0 and number < 8:
            result = result + str(number)
    return result[::-1]


def dec_to_hex(number):
    result = ""
    hex_dec_list = ['0', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while number > 1:
        if number % 16 == 0:
            result = result + str(0)
        else:
            result = result + str(hex_dec_list[(number % 16) - 1])
        number = int(number / 16)
        if number != 0 and number < 16:
            result = result + str(hex_dec_list[number - 1])
    return result[::-1]


def hex_to_dec_dic(value):
    hex_dec_dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    return hex_dec_dic[value]


def hex_to_bin(number):
    result = ""
    for n in number:
        if n == "A" or n == "B" or n == "C" or n == "D" or n == "E" or n == "F":
            result = result + dec_to_bin(hex_to_dec_dic(n), 16) + " "
        else:
            result = result + dec_to_bin(int(n), 16) + " "
    return result.rjust(20, '0')


def hex_to_oct(number):
    result = ""
    while number > 8:
        if number % 8 == 0:
            result = result + str(0)
        else:
            result = result + str(number % 8)
        number = int(number / 8)
        if number != 0 and number < 8:
            result = result + str(number)
    return result[::-1]


def hex_to_dec(number):
    number = number[::-1]
    result = 0
    count = 0
    for n in number:
        if n == "A" or n == "B" or n == "C" or n == "D" or n == "E" or n == "F":
            result += (hex_to_dec_dic(n) * (16 ** count))
        else:
            result += (int(n) * (16 ** count))
        count = count + 1
    return result


i = 1

while i == 1:
    option = menu()

    if option == 0:
        exit()
    elif option == 1:
        print("Binary to Decimal Conversion : ", bin_to_dec(get_number()))
    elif option == 2:
        print("Binary to Octal Conversion : ", bin_to_oct(bin_to_dec(get_number())))
    elif option == 3:
        print("Binary to Hexadecimal Conversion : ", bin_to_hex(bin_to_dec(get_number())))
    elif option == 4:
        print("Octal to Binary Conversion : ", oct_to_bin(get_number()))
    elif option == 5:
        print("Octal to Decimal Conversion : ", oct_to_dec(get_number()))
    elif option == 6:
        print("Octal to Hexadecimal Conversion : ", oct_to_hex(oct_to_dec(get_number())))
    elif option == 7:
        print("Decimal to Binary Conversion : ", dec_to_bin(int(get_number()), 0))
    elif option == 8:
        print("Decimal to Octal Conversion : ", dec_to_oct(int(get_number())))
    elif option == 9:
        print("Decimal to Hexadecimal Conversion : ", dec_to_hex(int(get_number())))
    elif option == 10:
        print("Hexadecimal to Binary Conversion : ", hex_to_bin(get_number()))
    elif option == 11:
        print("Hexadecimal to Octal Conversion : ", hex_to_oct(bin_to_dec(hex_to_bin(get_number()).replace(" ", ""))))
    elif option == 12:
        print("Hexadecimal to Decimal Conversion : ", hex_to_dec(get_number()))
