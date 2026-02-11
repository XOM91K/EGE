l=[[int(d) for d in x.split()] for x in open('1193.txt')]
for x in l:
    if len(set(x)) == 2:
        print(sum(x))