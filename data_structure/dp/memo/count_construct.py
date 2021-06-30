def countConstruct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            new_string = target[len(word):]
            num_ways = countConstruct(new_string, word_bank, memo)
            total_count += num_ways
    memo[target] = total_count
    return total_count


print(countConstruct('abcdef', ['ab', 'cd',
      'abc', 'def', 'abcd'], dict()))  # 1
print(countConstruct(
    'purple', ['p', 'purp', 'ur', 'le', 'purpl'], dict()))  # 2
print(countConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], dict()))  # 0
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                     [
                         'e',
                         'e'*5,
                         'e'*10,
                         'e'*7
                     ], dict()))
