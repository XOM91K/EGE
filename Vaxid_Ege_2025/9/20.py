l = [[int(d) for d in x.split()] for x in open('20.txt')]
for x in l:
    # pov = []
    # nepov = []
    # for y in x:
    #     if x.count(y) == 5:
    #         pov.append(y)
    #     if x.count(y) == 1:
    #         nepov.append(y)
    # if len(pov) == 5 and len(nepov) == 2:
    if len(set(x)) == 2:
        print(x, sum(x))
