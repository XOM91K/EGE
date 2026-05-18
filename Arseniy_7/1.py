N = int(input())
pr = 1
# 20 : 2, 4, 6, 8...18
for x in range(2, N + 1, 2):
    pr *= x
print(pr)
# 2 * 4 * 6