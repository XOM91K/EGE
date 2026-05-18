d = -1
ct = 0
while d != 0:
    d = int(input())
    if len(str(d)) == 3 and d % 4 == 0:
        ct += 1
print(ct)