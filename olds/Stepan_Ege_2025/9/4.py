l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    if (x[0] + x[-1]) % 3 == 0:
        if abs(x[0] - x[1]) == abs(x[2] - x[3]) or \
                abs(x[0] - x[2]) == abs(x[1] - x[3]) or \
                abs(x[0] - x[3]) == abs(x[2] - x[1]):

            print(x)