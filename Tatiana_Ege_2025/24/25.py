a = open(r"C:\Users\Zarif\Downloads\1483_1 (1).txt").readline()
b = a.split("CDE")
r = []
for i in range(len(b) - 85):
    try:
        p = b[i:i+86]
        k = b[i + 87]
        q = 0
        while k[q] == "E":
            q += 1
        else:
            q += 1
        s = 0
        for j in p:
            s += len(j)
        r.append(s + q)
    except:
        pass
print(min(r) + 87 * 3)