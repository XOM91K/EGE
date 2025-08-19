s = set()
for n in range (4,10000):
    x = '7' + '6' * n
    while '766' in x or '667' in x :
        if '766' in x :
            x = x.replace('766','67',1)
        if '667' in x:
            x = x.replace('667' , '7' , 1)
    s.add(x)
print(s)