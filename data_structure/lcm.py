
def getLCM(num1, num2):
    gcd = getGCD(num1, num2)
    lcm = (num1 * num2) // gcd
    return lcm


def LCM(arr):
    lcm = getLCM(arr[0], arr[1])
    for i in range(2, len(arr)):
        lcm = getLCM(lcm, arr[i])
    return lcm


def getGCD(num1, num2):
    while True:
        num1, num2 = num2, num1 % num2
        if num2 == 0:
            return num1


print(getLCM(12, 3))
print(LCM([12, 40, 96]))
