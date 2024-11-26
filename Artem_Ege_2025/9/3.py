l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    kr3 = [d for d in x if d % 3 == 0]
    if len(kr3) == 3:
        if abs(x[-1] - x[0]) <= sum(kr3):
            ct += 1
print(ct)
# l = [9, 2, 2, 2, 2, 3, 6, 1, 1, 1, 1, 2, 2, 2, 2]
# l2 = [x for x in l if x % 3 == 0]
# print(l2)