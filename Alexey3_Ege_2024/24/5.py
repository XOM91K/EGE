import string
alf = string.ascii_uppercase
print(alf)
s = open('5.txt').readlines()
mx_ln = 0
for x in s:
    x = x.strip()
    if x.count('A') < 25:
        for y in alf:
            if y in x:
                left = x.index(y)
                right = x.rindex(y)
                mx_ln = max(mx_ln, right - left)
print(mx_ln)