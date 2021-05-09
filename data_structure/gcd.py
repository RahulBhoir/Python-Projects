# euclidian
def getGCD(num1, num2):
    while True:
        num1, num2 = num2, num1 % num2
        if num2 == 0:
            return num1

# Recursive


def gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 > num2:
        return gcd(num1 % num2, num2)
    else:
        return gcd(num1, num2 % num1)


gcd = getGCD(15, 70)
print(gcd)
print(gcd(70, 15))
