a = [[int(i) for i in  x.split()] for x in open('16.txt')]
for i in range(len(a)):
    if a[i].count(max(a[i]))==3:
        nepovt = [y for y in a[i] if a[i].count(y) == 1]
        if len(nepovt) == 4:
            print(i+1, a[i], sum(a[i])/7)