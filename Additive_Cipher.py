choice = 1
while choice != 10:
    choice = int(input("1. Additive encrypt\n2. Additive decrypt\nSelect from above options: "))

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
        print("Decrypted text is: ",ct)
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
        print("Encrypted text is: ",pt)
        print()
    choice = int(input("To exit press 10 / TO continue press 1: "))