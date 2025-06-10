mass = 835 * 1000
l = [int(x) for x in open('12.txt') if 7000 <= int(x) <= 12000]
l = sorted(l, reverse=True)
gr = []
for x in l:
    if mass - x >= 0:
        mass -= x
        gr.append(x)
print(len(gr), gr[-1])
