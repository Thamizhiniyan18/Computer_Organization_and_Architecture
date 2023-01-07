# Function to get the number and base
def get_number_base():
    base = int(input("Enter the Base : "))
    if base == 10:
        number = int(input("Enter the Number : "))
    else:
        number = input("Enter the number : ")
    return number, base


def r_complementb(number):
    return str((bin(int(r1_complementb(number), 2) + 1)))[2:].zfill(len(str(number)))


def r1_complementb(number):
    if type(number) == str:
        string = ""
        for i in number:
            if i == "1":
                string += "0"
            else:
                string += "1"
        return string


def r1_complementd(number):
    n = number
    no_of_digits = 0
    while n > 0:
        n = n // 10
        no_of_digits += 1
    string = "9" * no_of_digits
    return int(string) - number


while True:
    print("Choose the option from the below list : ")
    print("""0 > Exit\n1 > r's Complement\n2 > (r-1)'s Complement\n3 > Both of the Operations""")
    option = int(input("Enter the Option : "))
    if option == 0:
        exit()
    elif option == 1:
        n, b = get_number_base()
        if (b == 2):
            _result = r_complementb(n)
        else:
            _result = r1_complementd(n) + 1
        print("The r's complement of the given number is : {}".format(_result))
    elif option == 2:
        n, b = get_number_base()
        if (b == 2):
            _result = r1_complementb(n)
        else:
            _result = r1_complementd(n)
        print("The (r-1)'s complement of the given number is : {}".format(_result))
    elif option == 3:
        n, b = get_number_base()
        if (b == 2):
            result1 = r1_complementb(n)
            result2 = r_complementb(n)
        else:
            result1 = r1_complementd(n)
            result2 = result1 + 1
        print("The r's complement of the given number is : {}".format(result2))
        print("The (r-1)'s complement of the given number is : {}".format(result1))
