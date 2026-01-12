l=[[int(d) for d in x.split()]for x in open('17.txt')]
for x in l:
    if x[0] < x[1] < x[2] < x[3] < x[4] < x[5] < x[6]:
        x=sorted(x)

        if (x[-1]-x[0])<(x[1]+x[2]+x[3]+x[4]):
            print(x[0]*x[1]*x[2]*x[3]*x[4]*x[5]*x[6])
            break