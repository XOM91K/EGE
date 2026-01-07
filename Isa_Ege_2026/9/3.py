l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    kr3 = [d for d in x if d % 3 == 0]
    if len(kr3) == 3:
        if max(x) - min(x) <= sum(kr3):
            print(x, kr3)
            ct += 1
print(ct)
# l = [33, 10, 7, 6]
# # [33, 6]
# kr3 = [x for x in l if x % 3 == 0]
# print(kr3)