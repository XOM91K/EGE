l = [int(x) for x in open('6.txt')]
ct = 0
sut = []
mel = []
for x in l:
    if x > 0:
        if str(x)[-1] == '4':
            mel.append(x)
mel = min(mel)
for x in range(len(l)-2):
    if (sum(map(int, str(abs(l[x])))) + sum(map(int, str(abs(l[x + 1])))) + sum(map(int, str(abs(l[x + 2]))))) % mel == 0:
        sut.append(l[x] + l[x+1] + l[x+2])
        ct += 1
print(ct,max(sut))