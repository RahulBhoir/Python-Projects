count = 0


def findPermutation(s, left, right):
    if left == right:
        temp = ''
        print(temp.join(s))
        global count
        count += 1
    else:
        for i in range(left, right):
            # do
            s[left], s[i] = s[i], s[left]
            # recur
            findPermutation(s, left+1, right)
            # undo
            s[left], s[i] = s[i], s[left]


s = input("enter the string: ")
s = list(s)
findPermutation(s, 0, len(s))
print('total permutation = ', count)
