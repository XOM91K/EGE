st = set()
kt = []
for x in range(0, 18):
    for y in range(9, 18):
        for x2 in range(0, y):
            for y2 in range(0, 18):
                c1 = 5 * 18 ** 3 + x * 18 ** 2 + y2 * 18 + 10
                c2 = 1 * y ** 3 + 8 * y ** 2 + x2 * y + 7
                if [c1, c2] not in kt:
                    st.add(c1 + c2)
                    kt.append([c1, c2])
print(len(st))