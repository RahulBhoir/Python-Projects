def encryption():
    pt = input("enter the plain text: ")
    key = int(input("enter the key: "))
    pt = list(pt)
    cypher_text = ""
    print()
    for x in pt:
        if x.isupper():
            # E = (x + n)mod 26
            temp = ((ord(x) - 65 + key) % 26) + 65
            cypher_text += chr(temp)
        if x.islower():
            temp = ((ord(x) - 97 + key) % 26) + 97
            cypher_text += chr(temp)
    return cypher_text


def decryption():
    cypher_text = input("enter the cipher text: ")
    key = int(input("enter the key: "))
    cypher_text = list(cypher_text)
    pt = ""
    print()
    for x in cypher_text:
        if x.isupper():
            # E = (x - n)mod 26
            temp = ((ord(x) - 65 - key) % 26) + 65
            pt += chr(temp)
        if x.islower():
            temp = ((ord(x) - 97 - key) % 26) + 97
            pt += chr(temp)
    return pt


choice = 1
while choice != 10:
    choice = int(input(
        "1. Additive encrypt\n2. Additive decrypt\nSelecypher_text from above options: "))

    if choice is 1:
        print(f"Encrypted text is: {encryption()} \n")
    elif choice is 2:
        print(f"Decrypted text is: {decryption()} \n")
    choice = int(input("To exit press 10 / TO continue press 1: "))
