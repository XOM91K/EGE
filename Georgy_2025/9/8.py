l = [[int(d) for d in x.split()] for x in open('8.txt')]
cnt = 0
for x in l:
    if x.count(min(x)) == 1:
        if len(set(x)) < 6:
            povt = [y for y in x if x.count(y) > 1]
            if max(x) + min(x) < sum(povt):
                cnt += 1
print(cnt)