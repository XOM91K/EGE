l = [int(x) for x in open('1.txt')]
ct = 0
for x in range(len(l) - 1):
    if l[x] % 2 == l[x + 1] % 2:
        ct += 1
print(ct)