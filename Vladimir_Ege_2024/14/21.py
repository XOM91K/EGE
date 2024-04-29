st = set()
for X in range(1, 1000):
    d = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** X - 2022
    if d > 0:
        s = []
        while d > 0:
            s.append(d % 4)
            d //= 4
        sm = s.count(1) + s.count(2) * 2 + s.count(3) * 3
        st.add(sm)
print(st)