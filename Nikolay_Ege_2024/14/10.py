st = []
for x in range(100):
    for y in range(100):
        if 9 <= y <= 17 and x <= 17 and x < y:
            c1 = 5 * 18 ** 3 + x * 18 ** 2 + y * 18 + 10
            c2 = 1 * y ** 3 + 8 * y ** 2 + x * y + 7
            st.append(c1 + c2)
print(len(set(st)))