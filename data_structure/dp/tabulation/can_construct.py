def canConstruct(target, word_bank):
    table = [False for i in range(len(target) + 1)]
    table[0] = True
    for i in range(len(target) + 1):
        if table[i] == True:
            for word in word_bank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] = True
    return table[len(target)]


print(canConstruct('abcdef', ['ab', 'cd', 'abc', 'def', 'abcd']))
print(canConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                   [
                       'e',
                       'e'*5,
                       'e'*10,
                       'e'*7
                   ]))
