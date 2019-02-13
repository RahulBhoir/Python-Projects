choice = 1
while choice != 10:
    choice = int(input("1.encrypt\n2.decrypt\nenter your choice: "))

    if choice == 1:

        pt = input("enter the plain text: ")
        ks = input("enter the key stream: ")
        pt = pt.lower()
        pt = list(pt)
        ks = list(ks)
        ct = ""

        if len(pt) == len(ks):
            pass
        else:
            t = len(pt) - len(ks)
            for x in range(t):
                ks.append(ks[x % t])

        for x in range(len(pt)):
            ks1 = ord(ks[x]) - 97
            pt1 = ord(pt[x]) - 97
            temp = (pt1 + ks1) % 26
            ct += chr(temp + 97)
        print("The encrypted text is : ",ct)
        print()

    elif choice == 2:

        ct = input("enter the cipher text: ")
        ks = input("enter the key stream: ")
        ct = ct.lower()
        ct = list(ct)
        ks = list(ks)
        pt = ""

        if len(ct) == len(ks):
            pass
        else:
            t = len(ct) - len(ks)
            for x in range(t):
                ks.append(ks[x % t])

        for x in range(len(ct)):
            ks1 = ord(ks[x]) - 97
            pt1 = ord(ct[x]) - 97
            temp = (pt1 + 26 - ks1) % 26
            pt += chr(temp + 97)
        print("The decrypted text is: ",pt)
        print()

    choice = int(input("10 to exit / 1 to continue: "))