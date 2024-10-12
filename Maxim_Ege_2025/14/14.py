st = set()
for x in range(18):
    for y in range(18):
        if x < y:
            c1 = 5 * 18 ** 3 + x * 18 ** 2 + y * 18 + 10
            c2 = 1 * y ** 3 + 8 * y ** 2 + x * y + 7
            st.add(c1 + c2)
print(len(st))