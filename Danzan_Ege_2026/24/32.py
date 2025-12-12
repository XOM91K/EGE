s = open(r'C:\Users\Zarif\Downloads\24_23381 (1).txt').readline()
for x in '02468':
    s = s.replace(x, '#')
s = s.split('#')
mx = []
for x in s:
    if len(set(x)) == 1:
        mx.append(len(x))
print(max(mx))