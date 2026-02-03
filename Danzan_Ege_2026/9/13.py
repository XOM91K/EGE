l = [[int(d) for d in x.split()] for x in open('13.txt')]
ct = 0
for x in l:
    x = sorted(x)
    povt = [d for d in x if 3 <= x.count(d) <= 4]
    nepovt = [d for d in x if x.count(d) == 1]
    if list(set(povt)) == [max(x)] and len(nepovt) == len(x) - len(povt):
        if nepovt[0] + nepovt[-1] <= sum(nepovt) - nepovt[0] - nepovt[-1]:
            ct += 1
print(ct)