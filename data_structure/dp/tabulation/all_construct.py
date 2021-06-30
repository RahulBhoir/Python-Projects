def allConstruct(target, word_bank):
    table = [[] for i in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:].startswith(word):
                new_combination = [combination + [word]
                                   for combination in table[i]]
                table[i + len(word)].extend(new_combination)

    return table[-1]


print(allConstruct('abcdef', ['cd', 'abc', 'def', ]))
print(allConstruct('abcdef', ['ab', 'cd', 'abc', 'def', 'abcd', 'ef', 'c']))
print(allConstruct(
    'purple', ['p', 'purp', 'ur', 'le', 'purpl']))
print(allConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                   [
                       'e',
                       'e'*5,
                       'e'*10,
                       'e'*7
                   ]))
