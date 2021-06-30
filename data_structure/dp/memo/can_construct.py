def canConstruct(target_string, word_bank, memo):
    if target_string in memo:
        return memo[target_string]
    if target_string == '':
        return True
    for word in word_bank:
        if target_string.startswith(word):
            new_string = target_string[len(word):]
            if canConstruct(new_string, word_bank, memo):
                memo[target_string] = True
                return True
    memo[target_string] = False
    return False


print(canConstruct('abcdef', ['ab', 'cd', 'abc', 'def', 'abcd'], dict()))
print(canConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], dict()))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                   [
                       'e',
                       'e'*5,
                       'e'*10,
                       'e'*7
                   ], dict()))
