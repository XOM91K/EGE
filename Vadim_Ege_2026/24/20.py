s = open(r'C:\Users\Zarif\Downloads\24_23206 (1).txt').readline()
for x in '02468':
    s = s.replace(x, '#')
s = s.split('#')
mx = []
for x in s:
    if x.count('S') >= 35:
        ln = ''
        for y in x:
            ln += y
            if ln.count('S') == 36:
                mx.append(len(ln))
                break
print(max(mx))