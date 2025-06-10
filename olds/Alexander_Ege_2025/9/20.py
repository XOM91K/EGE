ct = 0
l = [[int(d) for d in x.split()] for x in open("20.txt")]
for x in l:
    if len(set(x)) == len(x):
        nechetn = [i for i in x if i % 2 != 0]
        chetn = [i for i in x if i % 2 == 0]
        if len(nechetn) > len(chetn):
            if sum(nechetn) < sum(chetn):
                ct += 1
print(ct)
