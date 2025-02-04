s = open(r'C:\Users\Zarif\Downloads\329_1 (6).txt').readline()
mx_ln = 0
ts = ''
for x in s:
    ts += x
    if len(set(ts)) != len(ts):
        mx_ln = max(mx_ln, len(ts) - 1)
        ts = ts[ts.index(x) + 1:]
print(mx_ln)
