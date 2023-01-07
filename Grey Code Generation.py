# Decimal to Binary Conversion
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

    return result[::-1].rjust(base, '0')


def grey_code_generator(number):
    for i in range(0, 2 ** number):
        decimal_value = i ^ (i >> 1)
        grey_code = dec_to_bin(decimal_value, number)
        print(grey_code)


grey_code_generator(6)
