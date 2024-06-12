s = open(r'C:\Users\Zarif\Downloads\24_613_1 (1).txt').readline()
ct = 1
mx = 0
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)

# s = s.replace('RR', '@').replace('LL', '@').replace('DD', '@')
# s = s.split('@')
# #Определите максимальное количество
# # идущих подряд символов,
# # среди которых каждые два соседних различны.
# print(len(max(s, key=len)))
