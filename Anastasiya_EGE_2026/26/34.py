l = sorted([[int(d) for d in x.split()] for x in open('34.txt')])
mesta = ['0'] * 5700
# [0, 0, 0, 0, 0, 0, 0, 0]
for x in l:
    mesta[x[1] - 1] = '1'
    mesta_join = ''.join(mesta)
    if '000' in mesta_join:
        print(x[0], mesta_join.find('000') + 1)