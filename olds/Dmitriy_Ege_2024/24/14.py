import re, string
print(string.ascii_uppercase)
s = open(r'C:\Users\Zarif\Downloads\24_623_1 (1).txt').readline()
gl = 'BCDFGHJKLMNPQRSTVWXZ0123456789'
mx = 0
for x in '13579':
    r = s.split(x)
    for y in r:
        can = True
        for z in gl:
            if z in y:
                can = False
                break
        if can:
            mx = max(mx, len(y))
print(mx)