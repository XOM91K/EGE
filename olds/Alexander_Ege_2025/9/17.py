l = [[int(d) for d in x.split()] for x in open('17.txt')]
cnt = 0
for x in l:
    if len(set(x)) == 5:
        otr = [i for i in x if i < 0]
        pol = [i for i in x if i > 0]
        if abs(sum(otr)) > sum(pol):
            cnt += 1
print(cnt)