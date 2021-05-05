from reverse import ReverseNumber


def IsPanlindrone(number):
    reverse = ReverseNumber(number)
    if reverse == number:
        return True
    else:
        return False


print(IsPanlindrone(121))
