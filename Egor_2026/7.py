N = int(input())
mn = 10 ** 10
for x in range(N):
    a = int(input())
    if -1000 <= a <= 1000:
        if a % 5 == 0 or a % 8 == 0:
            if a < mn:
                mn = a
print(mn)