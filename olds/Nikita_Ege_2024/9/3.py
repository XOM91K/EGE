#249
l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    k = 0
    if len(set(x)) < len(x):
        k += 1
    if len([y for y in x if y % 2 == 1]) == 3:
        k += 1
    if k == 1:
        print(x)
        ct += 1
print(ct)