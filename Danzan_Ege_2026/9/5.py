l = [[int(d) for d in x.split()] for x in open ('5.txt')]
ct = 0

for x in l:
    chet = [d for d in x if d % 2 == 0]
    nechet = [d for d in x if d % 2 != 0]
    print(x, chet, nechet)
    k = 0
    if len(set(x)) == 4:
        k += 1
    if sum(nechet) > sum(chet):
        k += 1
    if k == 1:
            ct+=1
print(ct)
