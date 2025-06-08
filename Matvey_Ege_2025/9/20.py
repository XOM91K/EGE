l = [[int(y) for y in x.split()] for x in open('20.txt')]
ct = 0
for x in l:
    if x.count(max(x)) == 3 and len(set(x)) == 5:
        print(sum(x) / 7)