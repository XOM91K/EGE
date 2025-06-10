l = [[int(d) for d in x.split()] for x in open('24.txt')]
ct = 0
for x in l:
    if x.count(max(x)) == 1:
        if len(set(x)) < 6:
            if max(x) > ((sum(x) - max(x)) / 5) * 3:
                ct += 1
print(ct)

# d = [44, 44, 44, 44, 44, 44]
# print(set(d))
    #
    # print(x)