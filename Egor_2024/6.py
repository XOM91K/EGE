ct = 0
mx = 0
mn = 10 ** 10
for x in range(500):
    a = int(input())
    if -10000 <= a <= 200:
        if abs(a) % 2 == 0 or abs(a) % 10 != 7:
            ct += 1
            if a > mx:
                mx = a
            if a < mn:
                mn = a
print(ct, mx, mn)
