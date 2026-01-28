import re, string
l=[x.strip() for x in open('35.txt')]
d=[]
mx_ln = 0
for x in l:
    if x.count('A')<25:
        for y in string.ascii_uppercase:
            if y in x:
                mx_ln = max(mx_ln, x.rindex(y) - x.index(y))
print(mx_ln)