l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('3_a.txt')]
clusters = [[], [], []]
for x in l:
    if x[0] < 1 and x[1] > 0:
        clusters[0].append(x)
    elif x[0] < 1 and x[1] < 0:
        clusters[1].append(x)
    elif x[0] > 1:
        clusters[2].append(x)
srX = 0
srY = 0
for x in clusters[1]:
    srX += x[0]
    srY += x[1]
print(srX / len(clusters[1]), srY / len(clusters[1]))
#-2.6625289000000003     -2.505239333333332     5.23215396666667
#4.502584266666666       -4.270820599999998     -4.270820599999998

px = abs(int((-2.6625289000000003 -2.505239333333332 + 5.23215396666667) / 3 * 10000))
py = abs(int((4.502584266666666-4.270820599999998-4.270820599999998) / 3 * 10000))
print(4.502584266666666-4.270820599999998-4.270820599999998)
print(px, py)