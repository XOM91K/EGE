#HIOBIOHHAHOAHABHIAHIAHIHBHI
#d = open(r'test.txt').readline()
d = open(r'C:\Users\Zarif\Downloads\24_10131.txt').readline()
sl = {'A':{},'B':{}}
ctA = 0
ctB = 0
ct = {'A': 0, 'B': 0}
for x in range(len(d)):

    if d[x] == 'A':
        ctA += 1
    if d[x] == 'B':
        ctB += 1
    if ctA > ctB:
        if ctA - ctB not in sl['A']:
            sl['A'][ctA-ctB] = []
        sl['A'][ctA-ctB].append(x)
    elif ctA < ctB:
        if ctB - ctA not in sl['B']:
            sl['B'][ctB - ctA] = []
        sl['B'][ctB - ctA].append(x)
    # else:
    #     if ctA - ctB not in sl['A']:
    #         sl['A'][ctA-ctB] = []
    #     sl['A'][ctA-ctB].append(x)
    #     if ctB - ctA not in sl['B']:
    #         sl['B'][ctB - ctA] = []
    #     sl['B'][ctB - ctA].append(x)
mx = 0
for x in sl:
    for y in sl[x]:
        mx = max(mx, sl[x][y][-1] - sl[x][y][0])
print(mx)