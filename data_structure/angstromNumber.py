def AngstromNumber(number):
    # x = number
    # sum = 0
    # while number > 0:
    #     single_num = int(number % 10)
    #     sum += (single_num * single_num * single_num)
    #     number = int(number / 10)
    # if sum == x:
    #     print(True)
    # else:
    #     print(False)

    # pythonic way
    x = list(str(number))
    result = sum([int(i)**3 for i in x])
    ans = True if result == number else False
    return ans


number = 371
AngstromNumber(number)
