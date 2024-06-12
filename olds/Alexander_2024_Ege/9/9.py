l = [[int(d) for d in x.split()] for x in open('9.txt')]
def sosed(l, i, j):
    sp1 = l[i - 1:i]
    if len(sp1) != 0:
        sp1 = sp1[0]
    sd1 = []
    sd3 = []
    if len(sp1) == 1:
        sd1 = [sp1[j - 1: j], sp1[j], sp1[j + 1, j + 2]]
    sp2 = l[i]
    sd2 = [sp2[j - 1: j], sp2[j + 1: j + 2]]

    sp3 = l[i + 1: i + 2]
    if len(sp3) != 0:
        sp3 = l[i + 1: i + 2][0]
    g = sp3[j - 1: j]
    if len(sp3) != 0:
        sd3 = [sp3[j - 1: j][0], sp3[j], sp3[j + 1: j + 2][0]]
    sd = []
    for x in sd1 + sd2 + sd3:
        if type(x) != list:
            sd.append(x)
    return sd
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], sosed(l, i, j))
    break