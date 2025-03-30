#https://examinf.ru/tasks/167
l = [int(x) for x in open('10.txt')]
zak28 = [i for i in l if str(i)[-2:]=="28"]
mn =[]
sr = sum(zak28)/len(zak28)
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4 or len(str(abs(l[x + 2]))) == 4:
        zak11 = [i for i in [l[x], l[x + 1], l[x + 2]] if str(i)[-2:] == '11']
        if len(zak11) == 2:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                mn.append(sum([l[x], l[x + 1], l[x + 2]]))
print(len(mn), min(mn))