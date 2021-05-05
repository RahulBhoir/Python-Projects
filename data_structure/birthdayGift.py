n = 7
count = 0
# for i in range(1, n):
#     for j in range(1, n):
#         if j % i == 0:
#             print(i, j)
#             count += 1

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if j % i == 0 and k % j == 0:
                print(i, j, k)
                count += 1

print(count)
