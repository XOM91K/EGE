l=[[int(d) for d in x.split()]for x in open('23.txt')]
k=0
for x in l:
    k += 1
    if len(set(x)) == 2 and sum(set(x)) * 2 < sum(x) - sum(set(x)) * 2:
        print(k, x, sum(x))