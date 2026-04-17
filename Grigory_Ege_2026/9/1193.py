l = [[int(d) for d in x.split()] for x in open('1193.tt')]
for x in l:
    if len(set(x)) == 2: # 33 33 33 33 44 44 44
        print(x, sum(x))
