l = [int(x) for x in open('2.txt')]
sr = [x for x in l if str(x)[-3:] == '151']
sr = sum(sr) / len(sr)
ct = 0
mn = []
for x in range(len(l) - 2):
    st = [len(str(abs(y))) for y in [l[x], l[x + 1], l[x + 2]]]
    if st.count(4) in [1, 2]:
        kr13 = [y for y in [l[x], l[x + 1], l[x + 2]] if y % 13 == 0]
        kr7 = [y for y in [l[x], l[x + 1], l[x + 2]] if y % 7 == 0]
        if len(kr13) > len(kr7):
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(ct, min(mn))