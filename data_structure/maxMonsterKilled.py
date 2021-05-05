
def KillMonster(monsters, player_health, bonus):
    kills = 0
    length = len(monsters)
    for _ in range(len(monsters)):
        i = 0
        count = 0
        while i < length:
            if player_health >= monsters[i]:
                count += 1
                player_health += bonus[i]
                bonus.pop(i)
                monsters.pop(i)
                i -= 1
                length = len(monsters)
            i += 1
        if count != 0:
            kills += count
        else:
            return kills
    return kills


n = int(input())
player_health = int(input())
monsters = [int(input()) for i in range(n)]
bonus = [int(input()) for i in range(n)]

# monsters = [101, 100, 304]
# player_health = 100
# bonus = [100, 1, 500]

print(KillMonster(monsters, player_health, bonus))
