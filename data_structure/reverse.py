def ReverseNumber(number):
    reverse = 0
    count = 0
    while(number > 0):
        digit = int(number % 10)
        reverse = (reverse * 10) + digit
        number = int(number / 10)
        count += 1
    return reverse


print(ReverseNumber(1234))
