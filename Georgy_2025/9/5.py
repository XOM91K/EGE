l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
print(l)
for x in l:
    kr3 = [y for y in x if y % 3 == 0]
    if len(kr3) == 3:
        if max(x) - min(x) <= sum(kr3):
            ct += 1
print(ct)
# l = [1,2, 33, 444, 100 , 400, -500, 22, 1,1, 13,123,123, 2,1]
# d = [x for x in l if x % 2 == 0 and x > 300]
# print(l)
# print(d)