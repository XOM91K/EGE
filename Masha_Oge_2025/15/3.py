d = int(input())
mn = 10 ** 10
for x in range(d):
    a = int(input())
    if a % 10 == 2:
        mn = min(mn, a)
print(mn)