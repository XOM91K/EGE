a = [[int(d) for d in x.split()] for x in open('6.txt')]
# 5 5 5 5 5 3
c = 0
for e in a:
    if len(set(e)) == 2:
        s = sorted(e)
        if e.count(s[0]) > 1 and e.count(s[-1]) > 1:
            if s[0]+s[1]+s[5]+s[6] < s[2]+s[3]+s[4]:
                c += 1
                print(sum(e))
print(c)