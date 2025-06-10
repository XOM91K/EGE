l = [[int(d) for d in x.split()] for x in open('10.txt')]
N = [0] * 2
for x in l:
    for y in range(len(N)):
        if x[0] >= N[y]:
            N[y] = N[y] + x[1]
        else:
            #реализовать Вам.
print(N)
