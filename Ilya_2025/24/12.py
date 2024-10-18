s = open('12.txt').readline()
mx = 0
for x in '02468':
    st = s
    st = st.split(x)
    for y in range(1, len(st) - 1):
        g = sorted((set(st[y])))
        if ['F', 'K', 'L', 'N'] == g:
            mx = max(mx, len(st[y]))
print(mx)