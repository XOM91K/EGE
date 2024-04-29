l = sorted([int(x) for x in open('my673.txt')])
s = 100000
j = len(l) - 1
files = []
while j > 0:
    if s - l[j] >= 0:
        s -= l[j]
        files.append(l[j])
        if s - l[0] >= 0:
            s -= l[0]
            files.append(l[0])
            del l[0]
            j -= 1
    j -= 1
print(len(files), files[-1])