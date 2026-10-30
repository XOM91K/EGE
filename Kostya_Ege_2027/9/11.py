l = [[int(d) for d in x.split()] for x in open("11.txt")]
ct = 0
for x in l:
    povt3 = [d for d in x if x.count(d) >= 3]
    nepovt = [d for d in x if x.count(d) == 1]
    # 1 1 1 4 4 5
    if len(povt3) > 0 and len(nepovt) > 0:
        if (sum(x) -  sum(nepovt))/ (len(x) - len(nepovt)) < sum(nepovt) / len(nepovt):
            ct += 1
print(ct)