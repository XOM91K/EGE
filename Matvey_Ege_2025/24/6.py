s = open('174_1 (6).txt').readline()
f = '' #ABCDEFD
mx_ln = 0
for x in s:
    f += x
    if len(set(f)) != len(f):
        mx_ln = max(mx_ln, len(f) - 1)
        f = f[f.index(f[-1]) + 1:]
print(mx_ln)