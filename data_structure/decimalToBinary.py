
def DecimalToBinary(decimal_num):
    bin_num = ''
    decimal = list(str(decimal_num))
    power = 0

    if '.' in decimal:
        index = decimal.index('.')
        power = len(decimal) - index - 1
        print(power)
        decimal_num = int(decimal_num * (2**power))

    while True:
        remainder = decimal_num % 2
        bin_num += str(remainder)
        decimal_num = int(decimal_num / 2)
        if decimal_num <= 0:
            break
    bin_num = bin_num[::-1]

    # pythonic way
    # bin_num = bin(decimal_num)[2:]
    return int(bin_num)/(10**power)


def BinaryToDecimal(binary_num):
    binary_list = list(str(binary_num))
    integer_part = []
    fraction_part = []

    if '.' in binary_list:
        index = binary_list.index('.')
        for i in range(index):
            integer_part.append(int(binary_list[i]))

        for i in range(index + 1, len(binary_list)):
            fraction_part.append(int(binary_list[i]))

    integer_sum = 0
    for i in range(len(integer_part) - 1, -1, -1):
        multipy = 2**(len(integer_part) - i - 1)
        integer_sum += integer_part[i] * multipy

    fraction_sum = 0
    for i in range(len(fraction_part)):
        divide = 2**(i + 1)
        fraction_sum += fraction_part[i] * (1 / divide)

    decimal_number = integer_sum + fraction_sum
    return decimal_number


num = float(input("Enter a number: "))
value = input("press 'd' for decimal to binary else press 'b':")

if value == 'd':
    print(DecimalToBinary(num))
else:
    print(BinaryToDecimal(num))
