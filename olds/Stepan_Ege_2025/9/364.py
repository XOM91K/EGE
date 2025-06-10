l = [[int(d) for d in x.split()] for x in open('364.txt')]
ct = 0
for x in l:
    kr3 = [y for y in x if y % 3 == 0]
    if len(kr3) == 3:
        if max(x) - min(x) <= sum(kr3):
            ct += 1
            print(x, kr3)
print(ct)