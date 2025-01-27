l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        print(x)