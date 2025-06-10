# #364
l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    kr3 = [n for n in x if n % 3 == 0]
    if len(kr3) == 3:
        if x[-1] - x[0] <= sum(kr3):
            ct += 1
print(ct)
# x = [33, 18, 29, 40, 50, 100]
# print([d for d in x if d % 3 == 0])
# l = [9, 8, -5, -500, 250, 55]
# l2 = [x for x in l if x % 2 != 0 and x > 5 and x % 5 == 0]
# print(l2)
# d = [1, 9, 2]
# print(sum(d))