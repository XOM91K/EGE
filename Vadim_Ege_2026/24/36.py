l = open('36.txt').readlines()
m = 0
c = ''
for x in l:
    m = max(m,x.count('Q'))
for x in l:
    if x.count('Q') == m:
        c = x
m = 10**10
print(c)
c = c[:-1]
for x in c:
    m = min(m,c.count(x))
for x in c:
    if c.count(x)==m:
        print(x,m)
d = open('36.txt').read()
print(d.count('C'))