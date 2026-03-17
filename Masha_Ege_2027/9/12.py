l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    kr3 = [z for z in x if z % 3 == 0]
    if len(kr3) == 3:
        if max(x) - min(x) <= sum(kr3):
            ct += 1
print(ct)