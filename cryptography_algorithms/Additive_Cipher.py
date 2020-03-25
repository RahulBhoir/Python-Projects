def encryplain_textion():
    plain_text = 'rahul'  # input("enter the plain text: ")
    key = 5  # int(input("enter the key: "))
    plain_text = list(plain_text)
    cypher_text = ""
    print()
    for x in plain_text:
        if x.isupper():     # uppercase characypher_texters
            # E = (x + n)mod 26
            temp = ((ord(x) - 65 + key) % 26) + 65
            cypher_text += chr(temp)
        if x.islower():     # lowercase characypher_texters
            temp = ((ord(x) - 97 + key) % 26) + 97
            cypher_text += chr(temp)
    return cypher_text


def decryplain_textion():
    cypher_text = input("enter the cipher text: ")
    key = int(input("enter the key: "))
    cypher_text = list(cypher_text)
    plain_text = ""
    print()
    for x in cypher_text:
        if x.isupper():     # uppercase characypher_texters
            temp = ((ord(x) - 65 - key) % 26) + 65     # E = (x - n)mod 26
            plain_text += chr(temp)
        if x.islower():     # lowercase characypher_texters
            temp = ((ord(x) - 97 - key) % 26) + 97
            plain_text += chr(temp)
    return plain_text


choice = 1
while choice != 10:
    # int(input("1. Additive encryplain_text\n2. Additive decryplain_text\nSelecypher_text from above oplain_textions: "))
    choice = 1

    if choice is 1:
        # encrypt plain_text

        print("Decryplain_texted text is: ", encryplain_textion())
        print()
    elif choice is 2:
        # decrypt cypher_text
        print(f"Encryplain_texted text is: {decryplain_textion()}")
    choice = int(input("To exit press 10 / TO continue press 1: "))
