l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    if (list(set(x))[0] == 18 and len(set(x)) == 1) or (sum(x) % 18 == 0):
        ct += 1
print(ct)