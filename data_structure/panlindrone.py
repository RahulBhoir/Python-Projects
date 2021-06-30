def ReverseNumber(number):
    reverse = 0
    count = 0
    while(number > 0):
        digit = int(number % 10)
        reverse = (reverse * 10) + digit
        number = int(number / 10)
        count += 1
    return reverse


def IsPanlindrone(number):
    reverse = ReverseNumber(number)
    if reverse == number:
        return True
    else:
        return False

    # return True if str(number) == str(number)[::-1] else False


print(IsPanlindrone(1221))
