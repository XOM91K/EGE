a = [[int(i) for i in x.split()] for x in open('14.txt')]
ct = 0
for i in a:
    if max(i) < (sum(i) - max(i)):
        if len(set(i)) == 3:
            ct += 1
print(ct)