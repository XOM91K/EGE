l = sorted([[int(d) for d in x.split()] for x in open('5.txt')])
ct = 0
cases = [0] * 210
mn_case = 0
for x in l:
    for y in range(len(cases)):
        if x[0] > cases[y]:
            cases[y] = x[1]
            ct += 1
            mn_case = y + 1
            break

print(ct, mn_case)