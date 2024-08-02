l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    if sum(x) / 5 < (max(x) + min(x)) / 2:
        print(x)
        ct += 1
print(ct)