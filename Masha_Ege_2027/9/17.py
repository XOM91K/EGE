l = [[int(d) for d in x.split()] for x in open('17.txt')]
ct = 0
for x in l:
    tr = [y for y in x if x.count(y) >= 3] # список чисел которые повт 3 и более  раза
    od = [y for y in x if x.count(y) == 1] # список чисел которые повт 1 раз
    povt = [y for y in x if x.count(y) >= 2]
    if len(tr) > 0: # проверка на непустой список
        if len(od) > 0: # в строке есть число, не повторяющееся в этой строке
            if sum(povt) / len(povt) > sum(od) / len(od):
                ct += 1
print(ct)