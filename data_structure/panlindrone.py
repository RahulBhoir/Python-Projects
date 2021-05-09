from reverse import ReverseNumber


def IsPanlindrone(number):
    reverse = ReverseNumber(number)
    if reverse == number:
        return True
    else:
        return False

    # return True if str(number) == str(number)[::-1] else False


print(IsPanlindrone(1221))
