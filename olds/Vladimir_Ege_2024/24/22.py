s = open('22.txt').readline()
import string
print(string.ascii_uppercase)
for x in '02468BCDFGHJKLMNPQRSTVWXZ':
    s = s.replace(x, '#')
mx = 0
for x in '13579':
    d = s.split(x)
    #print(d)
    for x in d[1:-1]:
        if '#' not in x and len(x) > 0 and '1' not in x and '3' not in x and '5' not in x and '7' not in x and '9' not in x:
            mx = max(mx, len(x))
            print(x)
print(mx)