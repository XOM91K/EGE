s = open(r'C:\Users\Zarif\Downloads\24_11892.txt').readline()
#s = 'ZWXVUZVXZXVWWVWUZXX'
s = s.split('Y')
mn = 10 ** 10
ctx = [10000] * 499
for x in s:
    ct = 0
    for y in range(len(x)):
        if x[y] != 'X':
            ct += 1
        else:
            ctx.append(ct)
            ct = 0
            mn = min(mn, sum(ctx[-500:]))
print(mn + 500)