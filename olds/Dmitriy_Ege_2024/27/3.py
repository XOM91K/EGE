l = [int(x) for x in open('3.txt')]
ct = 0
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        if l[x] + l[y] >= 11023:
            ct += 1
print(ct)