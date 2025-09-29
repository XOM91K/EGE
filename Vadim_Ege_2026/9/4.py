l = [[int(d) for d in x.split()] for x in open("4.txt")]
ct = 0
for x in l:
    m = [i for i in x if i % 2 == 0]#chech
    k = [i for i in x if i % 2 != 0]#nech
    r = 0
    if len(set(x)) == 4:
        r += 1
    if sum(m) < sum(k):
        r += 1
    if r == 1:
        ct+=1
print(ct)