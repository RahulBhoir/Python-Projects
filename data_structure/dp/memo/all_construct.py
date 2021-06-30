def allConstruct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            new_string = target[len(word):]
            suffix_ways = allConstruct(new_string, word_bank, memo)
            target_ways = [way + [word] for way in suffix_ways]
            result.extend(target_ways)

    memo[target] = result
    return result


print(allConstruct('abcdef', ['ab', 'cd', 'abc', 'def', 'abcd'],
                   dict()))
print(allConstruct(
    'purple', ['p', 'purp', 'ur', 'le', 'purpl'], dict()))
print(allConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], dict()))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                   [
                       'e',
                       'e'*5,
                       'e'*10,
                       'e'*7
                   ], dict()))
