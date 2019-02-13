choice = 1
while choice != -1:

    choice = int(input("1. Additive Cipher\n2. Auto-Key Cipher\n -1 to exit\nSelect from above options: "))
    print()
    if choice is -1:
        exit()

    elif choice is 1:

        choice = int(input("1. Additive encrypt\n2. Additive decrypt\nSelect from above options: "))
        print()
        if choice is 1:
            # encrypt
            pt = input("enter the plain text: ")
            key = int(input("enter the key: "))
            pt = list(pt)
            ct = ""
            print()
            for x in pt:
                if x.isupper():     # uppercase characters
                    temp = (( ord(x) - 65 + key) % 26) + 65     # E = (x + n)mod 26
                    ct += chr(temp)
                if x.islower():     # lowercase characters
                    temp = (( ord(x) - 97 + key) % 26) + 97
                    ct += chr(temp)
            print("Encrypted text is: ",ct)
            print()

        elif choice is 2:
            # decrypt
            ct = input("enter the cipher text: ")
            key = int(input("enter the key: "))
            ct = list(ct)
            pt = ""
            print()
            for x in ct:
                if x.isupper():     # uppercase characters
                    temp = (( ord(x) - 65 - key) % 26) + 65     # E = (x - n)mod 26
                    pt += chr(temp)
                if x.islower():     # lowercase characters
                    temp = (( ord(x) - 97 - key) % 26) + 97
                    pt += chr(temp)
            print("Decrypted text is: ",pt)
            print()

    elif choice is 2:
        choice = int(input("1.encrypt\n2.decrypt\nenter your choice: "))
        print()
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
            print("The encrypted text is : ", ct)
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
            print("The decrypted text is: ", pt)
            print()

