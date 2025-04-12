l = [[int(d) for d in x.split()] for x in open("24.txt")]
k = 0
for x in l:
    k += 1
    chetn = [i for i in x if i % 2 == 0]
    nechetn = [i for i in x if i % 2 != 0]
    if len(nechetn) == len(chetn):
        x.sort()
        if x[0] + x[-1] == x[1] + x[-2] == x[2] + x[-3]:
            print(k, x)