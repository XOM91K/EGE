s=open(r'C:\Users\Zarif\Downloads\1415_1 (3).txt').readline()
s=s.split('X')
mn_ln=[]
for z in range(len(s) - 498):
    ln = 0
    kolvo_Y = 0
    for x in range(0, 499):
        ln += len(s[z + x])
        if 'Y' in s[z + x]:
            kolvo_Y = 1
    if kolvo_Y == 0:
        mn_ln.append(ln)
    if len(mn_ln) > 0:
        print(min(mn_ln) + 500)
print(min(mn_ln) + 500)