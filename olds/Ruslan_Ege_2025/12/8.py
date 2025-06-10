ct = 0
for N in range(12345, 13457):
    s = '1' * N
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)
        s = s.replace('1', '2', 1)
    if set(s) == {'2'}:
        ct += 1
print(ct)