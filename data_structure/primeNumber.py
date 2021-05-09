def IsPrimeNumber(number):
    divisor = 2
    while number > divisor:
        remainder = number % divisor
        if remainder == 0:
            return False
        divisor += 1
    return True


print(IsPrimeNumber(11))
