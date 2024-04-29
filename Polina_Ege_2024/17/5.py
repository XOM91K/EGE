l = [int(x) for x in open('17_4.txt')]
mn = 10**10
mx =0
ct =0

for x in l:
    if str(x)[-1] == '7':
        mn = min(mn,x)
for x in range(len(l) - 1):
    if ((abs(l[x]) % 10 == 7 and (abs(l[x+1])) % 10 != 7) or (abs(l[x]) % 10 != 7 and (abs(l[x+1])) % 10 == 7)) and (l[x]**2 + l[x+1]**2) < (mn ** 2):
        mx = max(mx, (l[x]**2+ l[x+1]**2))
        ct+=1

print(mn,ct, mx)